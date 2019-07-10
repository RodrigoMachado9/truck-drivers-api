from flask_restful import Resource, reqparse
from models.veiculo import VeiculoModel
#from models.site import SiteModel
#from resources.filtros import normalize_path_params, consulta_com_cidade, consulta_sem_cidade
from flask_jwt_extended import jwt_required
import sqlite3

path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)

class Veiculos(Resource):

    def get(self):

        #todo;  retornando uma lista de objetos.
        return {'Veiculos':[veiculo.json() for veiculo in VeiculoModel.query.all()]}

class Veiculo(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('marca', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('modelo')
    atributos.add_argument('placa')
    atributos.add_argument('ano')
    atributos.add_argument('cor')
    atributos.add_argument('tipo_de_carroceria')
    atributos.add_argument('numero_de_pallets')
    atributos.add_argument('cubagem_em_metros')
    atributos.add_argument('caminhao_possue_rastreador')
    atributos.add_argument('tipo_rastreador')
    atributos.add_argument('motorista_id', type=int, required=True, help="Every motorista needs to be linked veiculo.")



    def get(self, veiculo_id):
        veiculo = VeiculoModel.find_veiculo(veiculo_id)
        if veiculo:
            return veiculo.json()
        return {'message': 'veiculo not found.'}, 404

    @jwt_required
    def post(self, veiculo_id):
        if VeiculoModel.find_veiculo(veiculo_id):
            return {"message": "Type vehicle id '{}' already exists.".format(veiculo_id)}, 400 #Bad Request

        dados = Veiculo.atributos.parse_args()
        veiculo = VeiculoModel(**dados)


        """ composição
        if not MotoristaModel.find_by_id(dados['site_id']):
            return {'message': 'The hotel must be associated to a valid site id.'}, 400
        """
        try:
            veiculo.save_veiculo()
        except:
            #todo; cnh  =  unique.
            return {"message": "An error ocurred trying to create vehicle."}, 500 #Internal Server Error
        return veiculo.json(), 201

    @jwt_required
    def delete(self, veiculo_id):
        veiculo = VeiculoModel.find_veiculo(veiculo_id)
        if veiculo:
            veiculo.delete_veiculo()
            return {'message': 'Type vehicle deleted.'}
        return {'message': 'Type vehicle not found.'}, 404