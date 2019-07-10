from sql_alchemy import banco
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from datetime import datetime


#todo modelo da minha classe motorista
class VeiculoModel(banco.Model):
    __tablename__ = 'veiculo'

    veiculo_id = banco.Column(banco.Integer, primary_key = True)
    marca = banco.Column(banco.String(40))
    modelo = banco.Column(banco.String(40))
    placa = banco.Column(banco.String(40))
    ano = banco.Column(banco.String(40))
    cor = banco.Column(banco.String(40))
    tipo_de_carroceria = banco.Column(banco.String(40))
    numero_de_pallets = banco.Column(banco.String(40))
    cubagem_em_metros = banco.Column(banco.String(40))
    caminhao_possue_rastreador = banco.Column(banco.String(40)) #todo; transformar para tipo boolean
    tipo_rastreador = banco.Column(banco.String(40))
    motorista_id = banco.Column(banco.Integer, banco.ForeignKey('motoristas.motorista_id'))
    tipo_veiculo = banco.relationship('TipoVeiculoModel', backref='VeiculoModel', lazy='dynamic')
    status = banco.relationship('StatusModel', backref='VeiculoModel', lazy='dynamic')


    #site_id = banco.Column(banco.Integer, banco.ForeignKey('sites.site_id'))
    #site = banco.relationship('SiteModel')

    def __init__(self, marca, modelo, placa, ano, cor, tipo_de_carroceria,
                 numero_de_pallets,cubagem_em_metros,caminhao_possue_rastreador,
                 tipo_rastreador, motorista_id):

        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.tipo_de_carroceria = tipo_de_carroceria
        self.numero_de_pallets = numero_de_pallets
        self.cubagem_em_metros = cubagem_em_metros
        self.caminhao_possue_rastreador = caminhao_possue_rastreador
        self.tipo_rastreador = tipo_rastreador
        self.motorista_id = motorista_id


    #todo função que retornar o meu objeto em formato json !
    def json(self):
        return {
            'veiculo_id':self.veiculo_id,
            'marca':self.marca,
            'placa':self.placa,
            'ano':self.ano,
            'cor':self.cor,
            'tipo_de_carroceria': self.tipo_de_carroceria,
            'numero_de_pallets': self.numero_de_pallets,
            'cubagem_em_metros': self.cubagem_em_metros,
            'caminhao_possue_rastreador': self.caminhao_possue_rastreador,
            'tipo_do_rastreador': self.tipo_rastreador,
            'motorista_id':self.motorista_id,
            'tipo_do_veiculo':[tpveiculo.json() for tpveiculo in self.tipo_veiculo],
            'status_do_veiculo':[status.json() for status in self.status]
        }



    @classmethod
    def find_veiculo(cls, veiculo_id):
        # query, consulta o banco
        veiculo = cls.query.filter_by(veiculo_id=veiculo_id).first() # SELECT * FROM motorista WHERE motorista_id=id LIMIT 1
        if veiculo:
            return veiculo
        return None

    def save_veiculo(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_veiculo(self):
        banco.session.delete(self)
        banco.session.commit()