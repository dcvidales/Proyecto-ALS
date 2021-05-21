# coding: utf-8

import webapp2
import time

from model.casco import Casco


class EliminaEquipamientoHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        casco = Casco.recupera(self.request)
        casco.key.delete()
        time.sleep(1)
        return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/casco/elimina', EliminaEquipamientoHandler)
], debug=True)
