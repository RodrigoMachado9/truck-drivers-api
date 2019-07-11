__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

from sql_alchemy import banco
from models.aux import aux

#todo modelo da minha classe motorista
class LocalCargaModel(banco.Model):
    __tablename__ = 'local_carga'

    local_carga_id = banco.Column(banco.Integer, primary_key = True)
    endereco = banco.Column(banco.String(40))     #todo; true or false
    cidade = banco.Column(banco.String(40))     #todo; true or false
    avaliacao = banco.Column(banco.String(40))     #todo; aqui o cliente avalia determinado motorista...
    latitude = banco.Column(banco.String(40))
    longitude = banco.Column(banco.String(40))
    origem = banco.Column(banco.String(40))
    destino = banco.Column(banco.String(40))
    carga = banco.relationship('CargaModel')
    motorista_id = banco.Column(banco.Integer, banco.ForeignKey('motoristas.motorista_id'))
    transporte = banco.relationship('TransporteModel')




    def __init__(self, endereco, cidade, avaliacao,
                 latitude, longitude, origem, destino, motorista_id):

        #self.id = id
        self.endereco = endereco
        self.cidade = cidade
        self.avaliacao = avaliacao
        self.latitude = latitude
        self.longitude = longitude
        self.origem = origem
        self.destino = destino
        self.motorista_id = motorista_id


    #todo função que retornar o meu objeto em formato json !
    def json(self):
        return {
            'local_carga_id':self.local_carga_id,
            'endereco':self.endereco,
            'cidade':self.cidade,
            'avaliacao':self.avaliacao,
            'latitude':self.latitude,
            'longitude':self.longitude,
            'origem':self.origem,
            'destino':self.destino,
            'motorista_id':self.motorista_id,
            'transporte':[transporte.json() for transporte in self.transporte]
        }


    @classmethod
    def find_local_carga(cls, local_carga_id):
        # query, consulta o banco
        local_carga = cls.query.filter_by(local_carga_id=local_carga_id).first() # SELECT * FROM local_carga WHERE local_carga = local_carga LIMIT 1
        if local_carga:
            return local_carga
        return None

    def save_local_carga(self):
        banco.session.add(self)
        banco.session.commit()

    def update_local_carga(self, endereco, cidade, avaliacao, latitude, longitude, origem, destino):
        self.endereco = endereco
        self.cidade = cidade
        self.avaliacao = avaliacao
        self.latitude = latitude
        self.longitude = longitude
        self.origem = origem
        self.destino = destino

    def delete_local_carga(self):
        banco.session.delete(self)
        banco.session.commit()