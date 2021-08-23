class Activity():
    def __init__(self,
                 id,
                 name,
                 description,
                 type,
                 place,
                 organizator,
                 startDate,
                 startTime,
                 endDate,
                 endTime,
                 currentAttendees,
                 maxAttendees,
                 notes,
                 signups,
                 ):
        dayMap = {
            "22": 'st',
            "23": 'čt',
            "24": 'pá',
            "25": 'so',
            "26": 'ne',
        }
        
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.place = place
        self.organizator = organizator
        self.startDay = dayMap.get(startDate[:2], "")
        self.startTime = startTime
        self.endDay = dayMap.get(endDate[:2], "")
        self.endTime = endTime
        self.currentAttendees = currentAttendees
        self.maxAttendees = maxAttendees if maxAttendees != None else "neomezeno"
        self.notes = notes
        self.signups = signups
