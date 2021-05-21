from google.appengine.ext import ndb

from model.equipamiento import Equipamiento


class Avion(Equipamiento):
    cantidad = ndb.IntegerProperty(required=True)
    clase = ndb.StringProperty(required=True)
    velocidad_maxima = ndb.FloatProperty(required=True)

    @staticmethod
    def recupera_avion(req):
        try:
            id_ship = req.GET["ship"]
        except KeyError:
            id_ship = ""

        if id_ship:
            ship_key = ndb.Key(urlsafe=id_ship)
            avion = Avion.query(Avion.clave_barco == ship_key)
            return avion
        else:
            print("ERROR: Ship not found")
