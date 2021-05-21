# coding: utf-8


import webapp2
import time

from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.torpedo import Torpedo


class ModificaTorpedoHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        torp = Torpedo.recupera(self.request)

        valores_plantilla = {
            "clave_barco": clave_barco,
            "torp": torp
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_torpedo.html",
                                  **valores_plantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        torp = Torpedo.recupera(self.request)
        clave_barco = self.request.GET["ship"]
        cantidad = self.request.get("edCantidad", "") # Artillería//AA//Avion
        calibre = self.request.get("edCalibre", "") # Artillería//AA
        alcance = self.request.get("edAlcance", "") # Artillería//AA//Torpedo
        velocidad = self.request.get("edVelocidad", "") # Torpedo


        if (not (nombre) or not (cantidad) or not (calibre) or not (alcance)):
            return self.redirect("/")
        else:
            try:
                cantidad = int(cantidad)
                calibre = int(calibre)
                alcance = float(alcance)
                velocidad = float(velocidad)
            except ValueError:
                cantidad = -1
                calibre = -1
                alcance = -1
                velocidad = -1

            torp.nombre = nombre
            torp.cantidad = cantidad
            torp.calibre = calibre
            torp.alcance = alcance
            torp.velocidad = velocidad

            torp.put()

            time.sleep(1)
            return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/torpedo/modifica', ModificaTorpedoHandler)
], debug=True)
