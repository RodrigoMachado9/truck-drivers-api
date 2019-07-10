from flask_restful import Resource, reqparse
from models.tipo_veiculo import TipoVeiculoModel
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

class TipoVeiculos(Resource):

    def get(self):
        #todo;  retornando uma lista de objetos.
        return {'tipo_veiculos':[tpveiculo.json() for tpveiculo in TipoVeiculoModel.query.all()]}


class TipoVeiculo(Resource):

    atributos = reqparse.RequestParser()
    atributos.add_argument('documento', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('modal')
    atributos.add_argument('cargamin')
    atributos.add_argument('cargamax')
    atributos.add_argument('unidademedida')
    atributos.add_argument('totaleixos')
    atributos.add_argument('veiculo_id', type=int, required=True, help="Every tipo_do_veiculo needs to be linked veiculo_id.")


    def get(self, tipo_veiculo_id):
        tpveiculo = TipoVeiculoModel.find_tipo_veiculo(tipo_veiculo_id)
        if tpveiculo:
            return tpveiculo.json()
        return {'message': 'Tipo_veiculo not found.'}, 404

    @jwt_required
    def post(self, tipo_veiculo_id):
        if TipoVeiculoModel.find_tipo_veiculo(tipo_veiculo_id):
            return {"message": "Type vehicle id '{}' already exists.".format(tipo_veiculo_id)}, 400 #Bad Request

        dados = TipoVeiculo.atributos.parse_args()
        tpveiculo = TipoVeiculoModel(**dados)


        """ composição
        if not MotoristaModel.find_by_id(dados['site_id']):
            return {'message': 'The hotel must be associated to a valid site id.'}, 400
        """
        try:
            tpveiculo.save_tipo_veiculo()
        except:
            #todo; cnh  =  unique.
            return {"message": "An error ocurred trying to create data vehicle."}, 500 #Internal Server Error
        return tpveiculo.json(), 201


    @jwt_required
    def delete(self, tipo_veiculo_id):
        tpveiculo = TipoVeiculoModel.find_tipo_veiculo(tipo_veiculo_id)
        if tpveiculo:
            tpveiculo.delete_tipo_veiculo()
            return {'message': 'Type vehicle deleted.'}
        return {'message': 'Type vehicle not found.'}, 404