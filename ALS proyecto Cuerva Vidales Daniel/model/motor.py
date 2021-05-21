from google.appengine.ext import ndb

from model.equipamiento import Equipamiento


class Motor(Equipamiento):
    potencia = ndb.IntegerProperty(required=True)
    velocidad_maxima = ndb.FloatProperty(required=True)

    @staticmethod
    def recupera_motor(req):
        try:
            id_ship = req.GET["ship"]
        except KeyError:
            id_ship = ""

        if id_ship:
            ship_key = ndb.Key(urlsafe=id_ship)
            motor = Motor.query(Motor.clave_barco == ship_key)
            return motor
        else:
            print("ERROR: Ship not found")
