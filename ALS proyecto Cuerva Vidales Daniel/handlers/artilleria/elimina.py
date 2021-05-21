# coding: utf-8
# Nueva Barco

import webapp2
import time

from model.artilleria import Artilleria


class EliminaEquipamientoHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        artilleria = Artilleria.recupera(self.request)
        artilleria.key.delete()
        time.sleep(1)
        return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/artilleria/elimina', EliminaEquipamientoHandler)
], debug=True)
