class Entry():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    ## this is the constructor (__init__) constructs objects
   def __init__(self, id, date, concept, entry, moodId):
        self.id = id
        self.date = date
        self.concept = concept
        self.entry = entry
        self.moodId = moodId
        
