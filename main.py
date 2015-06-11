


import logging
import os
import webapp2
import jinja2

from model import Recording

def get_jinja_enviroment():
    return jinja2.Environment(
        loader= jinja2.FileSystemLoader(os.path.dirname(__file__) + "/views" ),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)
    
api_url = 'https://storage.googleapis.com'
default_version = 3

class BaseHandler(webapp2.RequestHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)

        self.template_values = {}
        self.template_values["live_editor"] = "../external/live-editor"
        self.jinja_enviroment = get_jinja_enviroment()
        
    # method used to set the
    def set_template(self, template):
        self.template = self.jinja_enviroment.get_template(template)

    def render(self):
        self.response.write(self.template.render(self.template_values))

class MainPage(BaseHandler):

    def get(self):

        recordings = Recording.query().fetch()
        self.set_template("index.html")
        
        self.template_values["recordings"] = recordings
        self.render()
        return

class SavePage(BaseHandler):
    def get(self):
        self.redirect("/")

    def post(self):
        
        post = self.request
        
        new_record = Recording(
            name= post.get("name", ""),
            playback= post.get("playback", ""),
            mp3 = post.get("mp3", ""))

        new_record.put()

        self.response.write(new_record.key.id())
        return

    def put(self):
        post = self.request
        recording = Recording.get_by_id(int(post.get("id")))

        if recording is not None:
            recording.mp3 = post.get("mp3", "")
            recording.put()
        else:
            self.error(404)


class RecordingPage(BaseHandler):
    def get(self, recording_id):
        recording = Recording.get_by_id(int(recording_id))

        if recording is None:
            self.redirect("/")
            return

        recordings = Recording.query().fetch()
        
        self.set_template("recording.html")
        
        self.template_values["recordings"] = recordings
        self.template_values["recording"] = recording
        self.render()
        return

    def delete(self, recording_id):
        
        recording = Recording.get_by_id(int(recording_id))

        if recording is not None:
            recording.key.delete()

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/save", SavePage),
    webapp2.Route("/recording/<recording_id>", handler=RecordingPage)

], debug=True)
