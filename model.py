


from google.appengine.ext import ndb

class Recording(ndb.Model):
    """basic type of model that all other inherit from
        mainly just a wrapper for ndb.Model
    """
    
    # the name of the recording
    name = ndb.StringProperty(indexed=True)

    # the list of commands for the playback
    playback = ndb.TextProperty()
    
    # url to the mp3 file
    mp3 = ndb.StringProperty(indexed=True)

    date_created = ndb.DateTimeProperty(indexed=True, auto_now_add=True)
