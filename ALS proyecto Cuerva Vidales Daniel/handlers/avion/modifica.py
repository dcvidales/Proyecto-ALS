# coding: utf-8


import webapp2
import time

from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.avion import Avion


class ModificaAvionHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        avion = Avion.recupera(self.request)

        valores_plantilla = {
            "clave_barco": clave_barco,
            "avion": avion
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_avion.html",
                                  **valores_plantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        avion = Avion.recupera(self.request)
        clave_barco = self.request.GET["ship"]
        cantidad = self.request.get("edCantidad", "")
        clase = self.request.get("edClase", "")
        v_avion = self.request.get("edVelocidadAvion", "")

        if (not (nombre) or not (cantidad) or not (clase) or not (v_avion)):
            return self.redirect("/")
        else:
            try:
                cantidad = int(cantidad)
                v_avion = float(v_avion)
            except ValueError:
                cantidad = -1
                v_avion = -1

            avion.nombre = nombre
            avion.cantidad = cantidad
            avion.clase = clase
            avion.velocidad_maxima = v_avion

            avion.put()

            time.sleep(1)
            return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/avion/modifica', ModificaAvionHandler)
], debug=True)
