from google.appengine.ext import ndb

from model.equipamiento import Equipamiento


class Artilleria(Equipamiento):
    cantidad = ndb.IntegerProperty(required=True)
    calibre = ndb.IntegerProperty(required=True)
    alcance = ndb.FloatProperty(required=True)

    @staticmethod
    def recupera_artilleria(req):
        try:
            id_ship = req.GET["ship"]
        except KeyError:
            id_ship = ""

        if id_ship:
            ship_key = ndb.Key(urlsafe=id_ship)
            artilleria = Artilleria.query(Artilleria.clave_barco == ship_key)
            return artilleria
        else:
            print("ERROR: Ship not found")
