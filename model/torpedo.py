from google.appengine.ext import ndb

from model.equipamiento import Equipamiento


class Torpedo(Equipamiento):
    cantidad = ndb.IntegerProperty(required=True)
    calibre = ndb.IntegerProperty(required=True)
    alcance = ndb.FloatProperty(required=True)
    velocidad = ndb.FloatProperty(required=True)

    @staticmethod
    def recupera_torp(req):
        try:
            id_ship = req.GET["ship"]
        except KeyError:
            id_ship = ""

        if id_ship:
            ship_key = ndb.Key(urlsafe=id_ship)
            torp = Torpedo.query(Torpedo.clave_barco == ship_key)
            return torp
        else:
            print("ERROR: Ship not found")
