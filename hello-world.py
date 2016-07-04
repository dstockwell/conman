import webapp2


class HelloWorld(webapp2.RequestHandler):
  def get(self, path):
    self.response.write('Hello, world.');

app = webapp2.WSGIApplication([
    webapp2.Route(r'/<:.*>', handler=HelloWorld),
])
