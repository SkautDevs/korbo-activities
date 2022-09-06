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
                 location,
                 ):
        dayMap = {
            "14": 'st',
            "15": 'čt',
            "16": 'pá',
            "17": 'so',
            "18": 'ne',
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
        self.location = location
