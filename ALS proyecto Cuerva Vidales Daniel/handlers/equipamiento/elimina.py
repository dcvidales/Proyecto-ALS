# coding: utf-8
# Nueva Barco

import webapp2
import time

from google.appengine.api import images
from webapp2_extras import jinja2

from model.equipamiento import Equipamiento


class EliminaEquipamientoHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        equipamiento = Equipamiento.recupera(self.request)
        equipamiento.key.delete()
        time.sleep(1)
        return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/equipamiento/elimina', EliminaEquipamientoHandler)
], debug=True)
