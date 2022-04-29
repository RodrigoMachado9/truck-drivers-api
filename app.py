__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

from flask import Flask, jsonify
from flask_restful import Api
#todo; resources
from resources.motorista import Motoristas, Motorista, MotoristasLocalCarga, CaminhoneirosVeiculoProprio, \
CaminhoneirosOrigemDestino, CaminhoneiroAvaliacao, CaminhoneirosDisponiveis

from resources.usuario import User, UserRegister, UserLogin, UserLogout, Users
from resources.tipoveiculo import TipoVeiculos, TipoVeiculo
from resources.veiculo import Veiculos, Veiculo

#todo; construir endpoint => veiculo, status_veiculo
from resources.statusveiculo import Status, StatusVeiculo
from resources.carga import Cargas, Carga
from resources.localcarga import LocalCargas, LocalCarga
from resources.transporte import Transportes, Transporte


# todo->  flask_jwt_extended :: será responsável por cuidar de toda parte de tokenização
from flask_jwt_extended import JWTManager

#todo guarda o token para futura verificação
from blacklist import BLACKLIST



app = Flask(__name__)

#todo sqlite -> migration to postgres
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///dummy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'hellotruck'
app.config['JWT_BLACKLIST_ENABLED'] = True


api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({"message":"You have been logged out!"}), 401  # unauthorized


#routes ...
api.add_resource(MotoristasLocalCarga, '/motoristas/local_carga/motoristas_sem_carga')

api.add_resource(CaminhoneirosVeiculoProprio, '/motoristas/motoristas_com_veiculo_proprio')

api.add_resource(CaminhoneirosOrigemDestino, '/motoristas/local_carga/veiculo/origem_destino')

api.add_resource(CaminhoneiroAvaliacao, '/motoristas/top_motoristas')

api.add_resource(CaminhoneirosDisponiveis, '/motoristas/status_veiculo/motoristas_disponiveis')

api.add_resource(Motoristas, '/motoristas')

api.add_resource(Motorista, '/motorista/<int:motorista_id>')

api.add_resource(Users, '/usuarios')

api.add_resource(User, '/usuarios/<int:user_id>')

api.add_resource(UserRegister, '/cadastro')

api.add_resource(UserLogin, '/login')

api.add_resource(UserLogout, '/logout')

api.add_resource(TipoVeiculos, '/tipo_veiculos')

api.add_resource(TipoVeiculo, '/tipo_veiculo/<int:tipo_veiculo_id>')

api.add_resource(Veiculos, '/veiculos')

api.add_resource(Veiculo, '/veiculo/<int:veiculo_id>')

api.add_resource(Status, '/status')

api.add_resource(StatusVeiculo, '/status_veiculo/<int:status_id>')

api.add_resource(Cargas, '/cargas')

api.add_resource(Carga, '/carga/<int:carga_id>')

api.add_resource(LocalCargas, '/local_cargas')

api.add_resource(LocalCarga, '/local_carga/<int:local_carga_id>')

api.add_resource(Transportes, '/transportes')

api.add_resource(Transporte, '/transporte/<int:transporte_id>')



if __name__ == '__main__':
    #todo debug == true, apenas enquanto em desenvolvimento.
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)
