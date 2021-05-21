# coding: utf-8
# Nueva Barco

import webapp2
import time

from webapp2_extras import jinja2

from model.barco import Barco

class NuevoBarcoHandler(webapp2.RequestHandler):
    def get(self):

        valores_plantilla = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_barco.html",
            **valores_plantilla))

    def post(self):
        clase = self.request.get("edClase", "Unknown")
        nombre = self.request.get("edNombre", "")
        pais = self.request.get("edPais", "")
        desc = self.request.get("edDesc","")


        if (not(clase) or not(nombre) or not(pais)):
            return self.redirect("/")

        barco = Barco(nombre=nombre, clase=clase, pais=pais, desc=desc)
        barco.put()
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/barco/nueva', NuevoBarcoHandler)
], debug=True)
