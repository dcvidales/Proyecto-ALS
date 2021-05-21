# coding: utf-8


import webapp2
import time

from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.casco import Casco


class ModificaCascoHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]
        casco = Casco.recupera(self.request)

        valores_plantilla = {
            "clave_barco": clave_barco,
            "casco": casco
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_casco.html",
                                  **valores_plantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        casco = Casco.recupera(self.request)
        clave_barco = self.request.GET["ship"]
        blindaje = self.request.get("edBlindaje", "")  # Casco
        ancho = self.request.get("edAncho", "")  # Casco
        largo = self.request.get("edLargo", "")  # Casco

        if (not (nombre) or not (blindaje) or not (ancho) or not (largo)):
            return self.redirect("/")
        else:
            try:
                blindaje = int(blindaje)
                ancho = float(ancho)
                largo = float(largo)
            except ValueError:
                blindaje = -1
                ancho = -1
                largo = -1

            casco.nombre = nombre
            casco.blindaje = blindaje
            casco.ancho = ancho
            casco.largo = largo

            casco.put()

            time.sleep(1)
            return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/casco/modifica', ModificaCascoHandler)
], debug=True)
