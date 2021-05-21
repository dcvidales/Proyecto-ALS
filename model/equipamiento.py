from google.appengine.ext import ndb

from model.barco import Barco


class Equipamiento(ndb.Model):
    tipo = ndb.StringProperty(indexed=True)
    nombre = ndb.StringProperty(required=True)
    clave_barco = ndb.KeyProperty(kind=Barco)

    @staticmethod
    def recupera_para(req):
        try:
            id_ship = req.GET["ship"]
        except KeyError:
            id_ship = ""

        if id_ship:
            ship_key = ndb.Key(urlsafe=id_ship)
            return ship_key.get()

        else:
            print("ERROR: Ship not found")

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()
