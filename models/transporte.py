__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

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
    chegada = banco.Column(banco.String(40))
    carga = banco.relationship('CargaModel')
    local_carga_id = banco.Column(banco.Integer, banco.ForeignKey('local_carga.local_carga_id'))


    def __init__(self, frete, incidente, chegada, local_carga_id):

        self.frete = frete
        self.incidente = incidente
        self.chegada = chegada
        self.local_carga_id = local_carga_id


    def json(self):
        return {
            'transporte_id':self.transporte_id,
            'frete':self.frete,
            'incidente':self.incidente,
            'chegada':self.chegada,
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
