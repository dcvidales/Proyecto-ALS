# coding: utf-8
# Nuevo Equipamiento

import webapp2
import time

from google.appengine.ext import ndb
from webapp2_extras import jinja2

from model.aa import AA
from model.artilleria import Artilleria
from model.torpedo import Torpedo
from model.casco import Casco
from model.motor import Motor
from model.avion import Avion


class NuevoEquipamientoHandler(webapp2.RequestHandler):
    def get(self):

        valores_plantilla = {
            "clave_barco": self.request.GET["ship"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_equipamiento.html",
                                  **valores_plantilla))

    def post(self):
        tipo = self.request.get("edTipo", "")
        nombre = self.request.get("edNombre", "")
        clave_barco = self.request.GET["ship"]
        cantidad = self.request.get("edCantidad", "") # Artillería//AA//Avion
        calibre = self.request.get("edCalibre", "") # Artillería//AA
        alcance = self.request.get("edAlcance", "") # Artillería//AA//Torpedo
        velocidad = self.request.get("edVelocidad", "") # Torpedo
        blindaje = self.request.get("edBlindaje", "") # Casco
        ancho = self.request.get("edAncho", "")  # Casco
        largo = self.request.get("edLargo", "") # Casco
        potencia = self.request.get("edPotencia", "") # Motor
        v_motor = self.request.get("edVelocidadMax", "")  # Motor
        a_class = self.request.get("edClase", "")  # Avion
        v_avion = self.request.get("edVelocidadAvion", "") # Avion

        if (not (tipo)):
            return self.redirect("/")
        elif (tipo == "AA"):
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

                aa = AA(tipo=tipo, nombre=nombre, clave_barco=ndb.Key(urlsafe=clave_barco), cantidad=cantidad,
                        calibre=calibre, alcance=alcance)
                aa.put()

        elif (tipo == "Artilleria"):
            print("Hola buenas tardes")
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

                artilleria = Artilleria(tipo=tipo, nombre=nombre, clave_barco=ndb.Key(urlsafe=clave_barco),
                                        cantidad=cantidad, calibre=calibre, alcance=alcance)
                artilleria.put()

        elif (tipo == "Torpedo"):
            if (not (nombre) or not (cantidad) or not (calibre) or not (alcance) or not (velocidad)):
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

                torpedo = Torpedo(tipo=tipo, nombre=nombre, clave_barco=ndb.Key(urlsafe=clave_barco),
                                  cantidad=cantidad, calibre=calibre, alcance=alcance, velocidad=velocidad)
                torpedo.put()

        elif (tipo == "Casco"):
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

                casco = Casco(tipo=tipo, nombre=nombre, clave_barco=ndb.Key(urlsafe=clave_barco),
                              blindaje=blindaje, ancho=ancho, largo=largo)
                casco.put()

        elif (tipo == "Motor"):
            if (not (nombre) or not (potencia) or not (v_motor)):
                return self.redirect("/")
            else:
                try:
                    potencia = int(potencia)
                    v_motor = float(v_motor)

                except ValueError:
                    potencia = -1
                    v_motor = -1
                motor = Motor(tipo=tipo, nombre=nombre, clave_barco=ndb.Key(urlsafe=clave_barco),
                              potencia=potencia, velocidad_maxima=v_motor)
                motor.put()

        elif (tipo == "Avion"):
            if (not (nombre) or not (a_class) or not (v_avion)):
                return self.redirect("/")
            else:
                try:
                    cantidad = int(cantidad)
                    v_avion = float(v_avion)
                except ValueError:
                    cantidad = -1
                    v_avion = -1

                avion = Avion(tipo=tipo, nombre=nombre, clave_barco=ndb.Key(urlsafe=clave_barco),
                              cantidad=cantidad, clase=a_class, velocidad_maxima=v_avion)
                avion.put()

        time.sleep(1)
        return self.redirect("/equipamiento/lista?ship=" + clave_barco)


app = webapp2.WSGIApplication([
    ('/equipamiento/nueva', NuevoEquipamientoHandler)
], debug=True)
