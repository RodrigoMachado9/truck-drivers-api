from flask_restful import Resource, reqparse
from models.status_veiculo import StatusModel
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

class Status(Resource):

    def get(self):

        #todo;  retornando uma lista de objetos.
        return {'Status_veiculo':[status.json() for status in StatusModel.query.all()]}

class StatusVeiculo(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('carregado')
    atributos.add_argument('pesocarga')
    atributos.add_argument('veiculo_id', type=int, required=True, help="Every motorista needs to be linked veiculo.")

    def get(self, status_id):
        status = StatusModel.find_status(status_id)
        if status:
            return status.json()
        return {'message': 'veiculo not found.'}, 404

    @jwt_required
    def post(self, status_id):
        if StatusModel.find_status(status_id):
            return {"message": "Type vehicle id '{}' already exists.".format(status_id)}, 400 #Bad Request

        dados = StatusVeiculo.atributos.parse_args()
        status = StatusModel(**dados)


        """ composição
        if not MotoristaModel.find_by_id(dados['site_id']):
            return {'message': 'The hotel must be associated to a valid site id.'}, 400
        """
        try:
            status.save_status()
        except:
            #todo; cnh  =  unique.
            return {"message": "An error ocurred trying to create vehicle."}, 500 #Internal Server Error
        return status.json(), 201

    @jwt_required
    def delete(self, status_id):
        status = StatusModel.find_status(status_id)
        if status:
            status.delete_status()
            return {'message': 'Type vehicle deleted.'}
        return {'message': 'Type vehicle not found.'}, 404