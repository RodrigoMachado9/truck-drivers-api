from sql_alchemy import banco
from sqlalchemy import DateTime
from datetime import datetime
from models.aux import aux

#todo modelo da minha classe motorista
class TransporteModel(banco.Model):
    __tablename__ = 'transporte'

    transporte_id = banco.Column(banco.Integer, primary_key = True)
    frete = banco.Column(banco.String(40))     #todo; true or false
    incidente = banco.Column(banco.String(40))     #todo; true or false
    partida = banco.Column(DateTime(), default=datetime.utcnow())
    chegada = banco.Column(DateTime(), default=datetime.utcnow())
    carga = banco.relationship('CargaModel')
    local_carga_id = banco.Column(banco.Integer, banco.ForeignKey('local_carga.local_carga_id'))


    def __init__(self, frete, incidente, local_carga_id):

        #self.id = id
        self.frete = frete
        self.incidente = incidente
        self.local_carga_id = local_carga_id


    #todo função que retornar o meu objeto em formato json !
    def json(self):
        return {
            'transporte_id':self.transporte_id,
            'frete':self.frete,
            'incidente':self.incidente,
            'carga':[carga.json() for carga in self.carga]

        }

    @classmethod
    def find_transporte(cls, transporte_id):
        # query, consulta o banco
        carga = cls.query.filter_by(transporte_id=transporte_id).first() # SELECT * FROM transporte WHERE transporte_id = transporte_id LIMIT 1
        if carga:
            return carga
        return None

    def save_transporte(self):
        banco.session.add(self)
        banco.session.commit()

    def update_transporte(self, frete, incidente):
        self.frete = frete
        self.incidente = incidente

    def delete_transporte(self):
        banco.session.delete(self)
        banco.session.commit()