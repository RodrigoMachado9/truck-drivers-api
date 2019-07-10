from sql_alchemy import banco

aux = banco.Table('aux',
                  banco.Column('motorista_id', banco.Integer, banco.ForeignKey('motoristas.motorista_id')),
                  banco.Column('transporte_id', banco.Integer, banco.ForeignKey('transporte.transporte_id')),
                  banco.Column('local_carga_id', banco.Integer, banco.ForeignKey('local_carga.local_carga_id')),
                  banco.Column('carga_id', banco.Integer, banco.ForeignKey('carga.carga_id')),
                  banco.Column('veiculo_id', banco.Integer, banco.ForeignKey('veiculo.veiculo_id'))
                  )

