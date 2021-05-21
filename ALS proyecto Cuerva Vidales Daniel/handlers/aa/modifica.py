# coding: utf-8


import webapp2
import time

from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.aa import AA


class ModificaAAHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        aa = AA.recupera(self.request)

        valores_plantilla = {
            "clave_barco": clave_barco,
            "aa": aa
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_aa.html",
                                  **valores_plantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        aa = AA.recupera(self.request)
        clave_barco = self.request.GET["ship"]
        cantidad = self.request.get("edCantidad", "")  # Artillería//AA//Avion
        calibre = self.request.get("edCalibre", "")  # Artillería//AA
        alcance = self.request.get("edAlcance", "")  # Artillería//AA//Torpedo

        if (not (nombre) or not (cantidad) or not (calibre) or not (alcance)):
            return self.redirect("/")
        else:
            try:
                cantidad = int(cantidad)
                calibre = int(calibre)
                alcance = float(alcance)
            except ValueError:
                cantidad = -1
                calibre = -1
                alcance = -1

            aa.nombre = nombre
            aa.cantidad = cantidad
            aa.calibre = calibre
            aa.alcance = alcance

            aa.put()

            time.sleep(1)
            return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/aa/modifica', ModificaAAHandler)
], debug=True)
