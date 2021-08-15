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
                 notes):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.place = place
        self.organizator = organizator
        self.startDate = startDate
        self.startTime = startTime
        self.endDate = endDate
        self.endTime = endTime
        self.currentAttendees = currentAttendees
        self.maxAttendees = maxAttendees if maxAttendees != None else "neomezeno"
        self.notes = notes
