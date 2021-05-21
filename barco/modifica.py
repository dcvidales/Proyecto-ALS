# coding: utf-8


import webapp2
import time

from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.barco import Barco


class ModificaBarcoHandler(webapp2.RequestHandler):
    def get(self):
        barco = Barco.recupera(self.request)

        valores_plantilla = {
            "barco": barco,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_barco.html",
                                  **valores_plantilla))

    def post(self):
        barco = Barco.recupera(self.request)
        clase = self.request.get("edClase", "Unknown")
        nombre = self.request.get("edNombre", "")
        pais = self.request.get("edPais", "")
        desc = self.request.get("edDesc", "")

        if (not (nombre) or not (pais) or not (clase)):
            return self.redirect("/")

        barco.nombre = nombre
        barco.pais = pais
        barco.clase = clase
        barco.desc = desc

        barco.put()

        time.sleep(1)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/barco/modifica', ModificaBarcoHandler)
], debug=True)
