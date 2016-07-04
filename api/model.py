from google.appengine.ext import ndb

class Con(ndb.Model):
  full_name = ndb.TextProperty()
  start = ndb.DateProperty()
  end = ndb.DateProperty()
  location = ndb.GeoPtProperty()
  address = ndb.TextProperty()
