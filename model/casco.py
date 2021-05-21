from google.appengine.ext import ndb

from model.equipamiento import Equipamiento


class Casco(Equipamiento):
    blindaje = ndb.IntegerProperty(required=True)
    ancho = ndb.FloatProperty(required=True)
    largo = ndb.FloatProperty(required=True)

    @staticmethod
    def recupera_casco(req):
        try:
            id_ship = req.GET["ship"]
        except KeyError:
            id_ship = ""

        if id_ship:
            ship_key = ndb.Key(urlsafe=id_ship)
            casco = Casco.query(Casco.clave_barco == ship_key)
            return casco
        else:
            print("ERROR: Ship not found")
