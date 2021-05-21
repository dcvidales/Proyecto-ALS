# coding: utf-8

import webapp2
import time

from model.motor import Motor


class EliminaEquipamientoHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        motor = Motor.recupera(self.request)
        motor.key.delete()
        time.sleep(1)
        return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/motor/elimina', EliminaEquipamientoHandler)
], debug=True)
