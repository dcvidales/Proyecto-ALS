# coding: utf-8

import webapp2
import time

from model.avion import Avion

class EliminaEquipamientoHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        avion = Avion.recupera(self.request)
        avion.key.delete()
        time.sleep(1)
        return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/avion/elimina', EliminaEquipamientoHandler)
], debug=True)
