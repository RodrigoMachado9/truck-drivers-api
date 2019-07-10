from sql_alchemy import banco
from models.aux import aux

#todo modelo da minha classe motorista
class MotoristaModel(banco.Model):
    __tablename__ = 'motoristas'

    motorista_id = banco.Column(banco.Integer, primary_key = True)
    nome = banco.Column(banco.String(40))
    idade = banco.Column(banco.Integer)
    rg = banco.Column(banco.String(10))
    orgaoemissor = banco.Column(banco.String(5))
    dataemissao = banco.Column(banco.String(10))
    datanascimento = banco.Column(banco.String(10))
    sexo = banco.Column(banco.String(1))
    cnh = banco.Column(banco.String(15), unique=True, nullable=False)
    cnhcategoria = banco.Column(banco.String(1))
    possueveiculoproprio = banco.Column(banco.String(10))
    transporte = banco.relationship('TransporteModel', secondary=aux, backref='subscribers', lazy='dynamic')
    carga = banco.relationship('CargaModel', secondary=aux, backref='subscribers', lazy='dynamic')
    veiculo = banco.relationship('VeiculoModel')
    localcarga = banco.relationship('LocalCargaModel')





    #site_id = banco.Column(banco.Integer, banco.ForeignKey('sites.site_id'))

    def __init__(self, nome, idade, rg, orgaoemissor, dataemissao,
                 datanascimento, sexo, cnh, cnhcategoria, possueveiculoproprio):

        #self.id = id
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self.orgaoemissor = orgaoemissor
        self.dataemissao = dataemissao
        self.datanascimento = datanascimento
        self.sexo = sexo
        self.cnh = cnh
        self.cnhcategoria = cnhcategoria
        self.possueveiculoproprio = possueveiculoproprio


    #todo função que retornar o meu objeto em formato json !
    def json(self):
        return {
            'motorista_id':self.motorista_id,
            'nome':self.nome,
            'idade':self.idade,
            'rg':self.rg,
            'orgao_emissor':self.orgaoemissor,
            'data_emissao':self.dataemissao,
            'data_nascimento':self.datanascimento,
            'sexo':self.sexo,
            'cnh':self.cnh,
            'cnh_categoria':self.cnhcategoria,
            'possue_veiculo_proprio':self.possueveiculoproprio,
            'veiculos':[veiculo.json() for veiculo in self.veiculo],
            'localcarga':[localcarga.json() for localcarga in self.localcarga],
            #'transporte':[subscriptions.json() for subscriptions in self.subscriptions]
        }



    @classmethod
    def find_motorista(cls, motorista_id):
        # query, consulta o banco
        motorista = cls.query.filter_by(motorista_id=motorista_id).first() # SELECT * FROM motorista WHERE motorista_id=id LIMIT 1
        if motorista:
            return motorista
        return None


    def save_motorista(self):
        banco.session.add(self)
        banco.session.commit()


    def update_motorista(self, nome, idade, rg, orgaoemissor, dataemissao,
                         datanascimento, sexo, cnh, cnhcategoria):
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self.orgaoemissor = orgaoemissor
        self.dataemissao = dataemissao
        self.datanascimento = datanascimento
        self.sexo = sexo
        self.cnh = cnh
        self.cnhcategoria = cnhcategoria

    def delete_motorista(self):
        banco.session.delete(self)
        banco.session.commit()