# coding: utf-8


import webapp2
import time

from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.motor import Motor


class ModificaMotorHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        motor = Motor.recupera(self.request)

        valores_plantilla = {
            "clave_barco": clave_barco,
            "motor": motor
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_motor.html",
                                  **valores_plantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        motor = Motor.recupera(self.request)
        clave_barco = self.request.GET["ship"]
        potencia = self.request.get("edPotencia","")
        v_motor = self.request.get("edVelocidadMax","")


        if (not (nombre) or not (potencia) or not (v_motor)):
            return self.redirect("/")
        else:
            try:
                potencia = int(potencia)
                v_motor = float(v_motor)

            except ValueError:
                potencia = -1
                v_motor = -1

            motor.nombre = nombre
            motor.potencia = potencia
            motor.velocidad_maxima = v_motor

            motor.put()

            time.sleep(1)
            return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/motor/modifica', ModificaMotorHandler)
], debug=True)
