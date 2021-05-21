from google.appengine.ext import ndb

from model.barco import Barco


class Comentario(ndb.Model):
    fecha = ndb.DateProperty(auto_now_add=True)
    usr = ndb.StringProperty(required=True)
    desc = ndb.StringProperty(required=True)
    clave_barco = ndb.KeyProperty(kind=Barco)

    @staticmethod
    def recupera_com(req):
        try:
            id_ship = req.GET["ship"]
        except KeyError:
            id_ship = ""

        if id_ship:
            ship_key = ndb.Key(urlsafe=id_ship)
            comentario = Comentario.query(Comentario.clave_barco == ship_key).order(-Comentario.fecha)
            return comentario
        else:
            print("ERROR: Ship not found")