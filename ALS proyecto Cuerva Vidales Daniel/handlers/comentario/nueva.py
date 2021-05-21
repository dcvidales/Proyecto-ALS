# coding: utf-8
# Nueva Barco

import webapp2
import time

from google.appengine.ext import ndb
from webapp2_extras import jinja2
from model.comentario import Comentario
from google.appengine.api import users

class NuevoComentarioHandler(webapp2.RequestHandler):
    def get(self):
        clave_barco = self.request.GET["ship"]

        valores_plantilla = {
            "clave_barco": clave_barco
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_comentario.html",
            **valores_plantilla))

    def post(self):
        usr = users.get_current_user().email()
        desc = self.request.get("edDesc","")
        clave_barco = self.request.GET["ship"]


        if (not(usr) or not(desc)):
            return self.redirect("/")

        comentario = Comentario(usr=usr, desc=desc, clave_barco=ndb.Key(urlsafe=clave_barco) )
        comentario.put()
        time.sleep(1)
        return self.redirect("/equipamiento/lista?ship=" + clave_barco)

app = webapp2.WSGIApplication([
    ('/comentario/nueva', NuevoComentarioHandler)
], debug=True)
