# coding: utf-8
# Nueva Barco

import webapp2
import time

from google.appengine.api import images
from webapp2_extras import jinja2

from model.barco import Barco


class EliminaBarcoHandler(webapp2.RequestHandler):
    def get(self):
        barco = Barco.recupera(self.request)
        barco.key.delete()
        time.sleep(1)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/barco/elimina', EliminaBarcoHandler)
], debug=True)
