from sql_alchemy import banco
from models.aux import aux

#todo modelo da minha classe motorista
class CargaModel(banco.Model):
    __tablename__ = 'carga'

    carga_id = banco.Column(banco.Integer, primary_key = True)
    categoria = banco.Column(banco.String(40))                      #todo; cargas frágeis, cargas vivas
    inflamavel = banco.Column(banco.String(40))     #todo; true or false
    local_carga_id = banco.Column(banco.Integer, banco.ForeignKey('local_carga.local_carga_id'))
    transporte_id = banco.Column(banco.Integer, banco.ForeignKey('transporte.transporte_id'))


    def __init__(self, categoria, inflamavel, local_carga_id, transporte_id):

        #self.id = id
        self.categoria = categoria
        self.inflamavel = inflamavel
        self.local_carga_id = local_carga_id
        self.transporte_id = transporte_id


    #todo função que retornar o meu objeto em formato json !
    def json(self):

        return {
            'carga_id':self.carga_id,
            'categoria':self.categoria,
            'inflamavel':self.inflamavel,

        }


    @classmethod
    def find_carga(cls, carga_id):
        # query, consulta o banco
        carga = cls.query.filter_by(carga_id=carga_id).first() # SELECT * FROM carga WHERE carga_id = carga_id LIMIT 1
        if carga:
            return carga
        return None

    def save_carga(self):
        banco.session.add(self)
        banco.session.commit()

    def update_carga(self, categoria, inflamavel):
        self.categoria = categoria
        self.inflamavel = inflamavel

    def delete_carga(self):
        banco.session.delete(self)
        banco.session.commit()