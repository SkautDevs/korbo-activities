import csv
import glob
import os
import pdfkit

from Activity import Activity
from jinja2 import Environment, select_autoescape

def getEventFilename(dir_path):
    return glob.glob(dir_path + "/tables/events-*.csv")[0]

def getSignupsFilename(dir_path):
    return glob.glob(dir_path + "/tables/signups-*.csv")[0]


def mapRowToActivity(row, signups):
    return Activity(
        row[0],
        row[1],
        row[16],
        None,
        row[7],
        row[14] + row[17],
        row[2],
        row[3],
        row[4],
        row[5],
        None,
        None,
        None,
        signups.get(row[1], []),
        row[15],
    )


def generateHtml(activity):
    env = Environment(
        autoescape=select_autoescape()
    )
    
    templateFile = open("activityTemplate.jinja2", "r")
    template = env.from_string(templateFile.read())
    
    return template.render(a=activity)


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    signupsCsv = getSignupsFilename(dir_path)
    signups = {}
    with open(signupsCsv) as csv_signups_file:
        next(csv_signups_file)
        csv_reader = csv.reader(csv_signups_file, delimiter=',')
        for row in csv_reader:
            signup = signups.get(row[1], [])
            signup.append(row[3])
            signups[row[1]] = signup
    
    eventCsv = getEventFilename(dir_path)
    activities = []
    with open(eventCsv) as csv_events_file:
        next(csv_events_file)
        csv_reader = csv.reader(csv_events_file, delimiter=',')
        for row in csv_reader:
            activities.append(mapRowToActivity(row, signups))
    
    count = 0
    for activity in activities:
        count += 1
        print("Generating " + str(count) +  ". from " + str(len(activities)))
        html = generateHtml(activity)
        htmlFile = open("htmlOutput/generated.html", "w")
        htmlFile.write(html)
        htmlFile.close()

        output_path = dir_path + "/pdfOutput/generated_" + activity.id + ".pdf"
        pdfkit.from_file(htmlFile.name, output_path, options={"encoding": "UTF-8","page-size": "A5",})
        print("Done " + str(count) +  ". from " + str(len(activities)))
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
