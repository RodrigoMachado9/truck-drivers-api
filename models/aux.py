__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

from sql_alchemy import banco

aux = banco.Table('aux',
                  banco.Column('motorista_id', banco.Integer, banco.ForeignKey('motoristas.motorista_id')),
                  banco.Column('transporte_id', banco.Integer, banco.ForeignKey('transporte.transporte_id')),
                  banco.Column('local_carga_id', banco.Integer, banco.ForeignKey('local_carga.local_carga_id')),
                  banco.Column('carga_id', banco.Integer, banco.ForeignKey('carga.carga_id')),
                  banco.Column('veiculo_id', banco.Integer, banco.ForeignKey('veiculo.veiculo_id'))
                  )

