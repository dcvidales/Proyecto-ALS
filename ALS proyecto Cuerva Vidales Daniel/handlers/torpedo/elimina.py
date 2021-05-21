# coding: utf-8

import webapp2
import time

from model.torpedo import Torpedo


class EliminaEquipamientoHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        torpedo = Torpedo.recupera(self.request)
        torpedo.key.delete()
        time.sleep(1)
        return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/torpedo/elimina', EliminaEquipamientoHandler)
], debug=True)
