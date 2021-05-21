# coding: utf-8
# Asignatura perteneciente a un año academico
# Esto vendria siendo la clase barco en la que se indexarian por clases y contendria el nombre

from google.appengine.ext import ndb


class Barco(ndb.Model):
    clase = ndb.StringProperty(indexed=True)
    pais = ndb.StringProperty(required=True)
    nombre = ndb.StringProperty(required=True)
    desc = ndb.StringProperty()

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()
