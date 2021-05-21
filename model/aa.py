from google.appengine.ext import ndb

from model.equipamiento import Equipamiento


class AA(Equipamiento):
    cantidad = ndb.IntegerProperty(required=True)
    calibre = ndb.IntegerProperty(required=True)
    alcance = ndb.FloatProperty(required=True)

    @staticmethod
    def recupera_aa(req):
        try:
            id_ship = req.GET["ship"]
        except KeyError:
            id_ship = ""

        if id_ship:
            ship_key = ndb.Key(urlsafe=id_ship)
            aa = AA.query(AA.clave_barco == ship_key)
            return aa
        else:
            print("ERROR: Ship not found")