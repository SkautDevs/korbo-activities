import csv
import glob
import os
import pdfkit

from Activity import Activity
from jinja2 import Environment, PackageLoader, select_autoescape

def getEventFilename(dir_path):
    return glob.glob(dir_path + "/tables/events-*.csv")[0]

def getSignupsFilename(dir_path):
    return glob.glob(dir_path + "/tables/signups-*.csv")[0]


def mapRowToActivity(row):
    return Activity(
        row[0],
        row[1],
        row[15],
        row[16],
        row[7],
        row[14],
        row[2],
        row[3],
        row[4],
        row[5],
        None,
        None,
        row[15]
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
    
    eventCsv = getEventFilename(dir_path)
    activities = []
    
    with open(eventCsv) as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=',')
        headerFlag = True
        for row in csv_reader:
            if headerFlag == True:
                headerFlag = False
                continue
            
            activities.append(mapRowToActivity(row))
    
    for activity in activities:
        html = generateHtml(activity)
        htmlFile = open("htmlOutput/generated.html", "w")
        htmlFile.write(html)
        htmlFile.close()

        output_path = dir_path + "/pdfOutput/generated_" + activity.id + ".pdf"
        pdfkit.from_file(htmlFile.name, output_path, options={'encoding': "UTF-8",'page-size': 'A5',})
    
    signupCsv = getSignupsFilename(dir_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
