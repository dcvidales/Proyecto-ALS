# coding: utf-8

import webapp2
import time

from model.aa import AA


class EliminaEquipamientoHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        aa = AA.recupera(self.request)
        aa.key.delete()
        time.sleep(1)
        return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/aa/elimina', EliminaEquipamientoHandler)
], debug=True)
