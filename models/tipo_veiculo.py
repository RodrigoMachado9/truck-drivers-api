__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

from sql_alchemy import banco

#todo modelo da minha classe motorista
class TipoVeiculoModel(banco.Model):
    __tablename__ = 'tipo_veiculo'

    tpveiculo_id = banco.Column(banco.Integer, primary_key = True)
    documento = banco.Column(banco.String(40))
    modal = banco.Column(banco.String(40))
    cargamin = banco.Column(banco.Integer)
    cargamax = banco.Column(banco.Integer)
    unidademedida = banco.Column(banco.String(2))
    totaleixos = banco.Column(banco.String(20))
    veiculo_id = banco.Column(banco.Integer, banco.ForeignKey('veiculo.veiculo_id'))


    def __init__(self, documento,
                  modal, cargamin, cargamax, unidademedida, totaleixos, veiculo_id):

        self.documento = documento
        self.modal = modal
        self.cargamin = cargamin
        self.cargamax = cargamax
        self.unidademedida = unidademedida
        self.totaleixos = totaleixos
        self.veiculo_id = veiculo_id


    def json(self):
        return {
            'tipo_veiculo_id':self.tpveiculo_id,
            'documento':self.documento,
            'modal':self.modal,
            'carga_minima':self.cargamin,
            'carga_maxima':self.cargamax,
            'unidade_de_medida':self.unidademedida,
            'total_de_eixos':self.totaleixos,
            'veiculo_id':self.veiculo_id
            }

    @classmethod
    def find_tipo_veiculo(cls, tpveiculo_id):
        # query, consulta o banco
        tpveiculo = cls.query.filter_by(tpveiculo_id=tpveiculo_id).first() # SELECT * FROM tipo_veiculo WHERE id=id LIMIT 1
        if tpveiculo:
            return tpveiculo
        return None

    def save_tipo_veiculo(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_tipo_veiculo(self):
        banco.session.delete(self)
        banco.session.commit()
