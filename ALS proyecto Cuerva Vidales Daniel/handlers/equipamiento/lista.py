import webapp2
from webapp2_extras import jinja2


from model.aa import AA
from model.artilleria import Artilleria
from model.avion import Avion
from model.casco import Casco
from model.comentario import Comentario
from model.equipamiento import Equipamiento
from model.motor import Motor
from model.torpedo import Torpedo


class ListaEquipamientoHandler(webapp2.RequestHandler):
    def get(self):
        barco = Equipamiento.recupera_para(self.request)
        aa = AA.recupera_aa(self.request)
        artilleria = Artilleria.recupera_artilleria(self.request)
        avion = Avion.recupera_avion(self.request)
        casco = Casco.recupera_casco(self.request)
        motor = Motor.recupera_motor(self.request)
        torp = Torpedo.recupera_torp(self.request)
        comentario = Comentario.recupera_com(self.request)

        valores_plantilla = {
            "barco": barco,
            "aa": aa,
            "artilleria": artilleria,
            "avion": avion,
            "casco": casco,
            "motor": motor,
            "torp": torp,
            "comentario": comentario
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("lista_equipamiento.html",
                                  **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/equipamiento/lista', ListaEquipamientoHandler)
], debug=True)