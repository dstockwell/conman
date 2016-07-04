from google.appengine.ext import ndb
from google.appengine.ext import db

import datetime
import webapp2
import json

from model import Con

class Setup(webapp2.RequestHandler):
  def get(self, name):
    con = Con(id=name.lower())
    con.full_name = 'BlinkOn 7'
    con.start = datetime.date(2017, 1, 11)
    con.end = datetime.date(2017, 1, 12)
    con.location = db.GeoPt(37.4037412,-122.034507)
    con.address = db.Text('803 11th Ave, Sunnyvale, CA 94089, United States')
    con.put()
    self.response.write('OK')

class GetCon(webapp2.RequestHandler):
  def get(self, name):
    con = Con.get_by_id(name.lower(), read_policy=ndb.EVENTUAL_CONSISTENCY)
    if con is None:
      self.response.write("No conference named '%s' available" % (name))
      return
    self.response.headers['Content-Type'] = 'text/json'
    self.response.write(json.dumps({
      'name': name,
      'full_name': con.full_name,
      'start': con.start.isoformat(),
      'end': con.end.isoformat(),
    }));

app = webapp2.WSGIApplication([
    webapp2.Route(r'/<name>/api/setup', handler=Setup),
    webapp2.Route(r'/<name>/api/con', handler=GetCon),
], debug=True)
