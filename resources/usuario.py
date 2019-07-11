__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

from flask_restful import Resource, reqparse
from models.usuario import UserModel
#todo para construç~ao e verificação do token....
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from blacklist import BLACKLIST

#todo -> .:definindo atributos como variável global.:
atributos = reqparse.RequestParser()
atributos.add_argument('login', required=True, help="The field 'login' cannot be left ")
atributos.add_argument('senha', required=True, help="The field 'senha' cannot be left ")

class User(Resource):

    # todo -> /usuarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message':'User not foud.'}, 404   #todo not found

    @jwt_required   #todo -> será obrigatorio estar logado para deletar determinado usuario.
    def delete(self, user_id):

        user = UserModel.find_user(user_id)

        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'An internal error occured trying to delete user.'}, 500  # internal server error
            return {'message':'User deleted.'}
        return {'message':'User not found.'}, 404 # hotel não encontrado


class UserRegister(Resource):

    #todo -> /cadastro

    def post(self):
        dados = atributos.parse_args()

        #todo verificando se o usuario ja existe
        if UserModel.find_by_login(dados['login']):
            return {"message":"The login '{}' alredy exists.".format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {"message":"User created successfully!"}, 201 # created


class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access token':token_de_acesso}, 200
        return {'message':'The username or password is incorrect! '}, 401 #Unathorized!



class UserLogout(Resource):

    @jwt_required
    def post(cls):
        jwt_id = get_raw_jwt()['jti'] # jwt Token Identifier
        BLACKLIST.add(jwt_id)
        return {"message":"Logged out successfully!"}, 200