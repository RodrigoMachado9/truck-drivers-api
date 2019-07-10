from sql_alchemy import banco
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from datetime import datetime


#todo modelo da minha classe motorista
class StatusModel(banco.Model):
    __tablename__ = 'status_veiculo'

    status_id = banco.Column(banco.Integer, primary_key = True)
    carregado = banco.Column(banco.String(40))
    pesocarga = banco.Column(banco.String(40))
    veiculo_id = banco.Column(banco.Integer, banco.ForeignKey('veiculo.veiculo_id'))

    #site_id = banco.Column(banco.Integer, banco.ForeignKey('sites.site_id'))
    #site = banco.relationship('SiteModel')

    def __init__(self, carregado, pesocarga, veiculo_id):

        self.carregado = carregado
        self.pesocarga = pesocarga
        self.veiculo_id = veiculo_id



    #todo função que retornar o meu objeto em formato json !
    def json(self):
        return {
            'status_id':self.status_id,
            'veiculo_carregado':self.carregado,
            'peso_da_carga':self.pesocarga,
            'veiculo_id':self.veiculo_id,
        }

    @classmethod
    def find_status(cls, status_id):
        # query, consulta o banco
        status = cls.query.filter_by(status_id=status_id).first() # SELECT * FROM status_veiculo WHERE status_id=status_id LIMIT 1
        if status:
            return status
        return None

    def save_status(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_status(self):
        banco.session.delete(self)
        banco.session.commit()