from flask_restful import Resource, reqparse
from models.carga import CargaModel
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

class Cargas(Resource):

    def get(self):
        #todo;  retornando uma lista de objetos.
        return {'cargas':[carga.json() for carga in CargaModel.query.all()]}


class Carga(Resource):

    atributos = reqparse.RequestParser()
    atributos.add_argument('categoria', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('inflamavel')
    atributos.add_argument('local_carga_id', type=int, required=True, help="Every carga needs to be linked local_carga.")
    atributos.add_argument('transporte_id', type=int, required=True, help="Every carga needs to be linked transporte.")


    def get(self, carga_id):
        carga = CargaModel.find_carga(carga_id)
        if carga:
            return carga.json()
        return {'message': 'carga not found.'}, 404

    @jwt_required
    def post(self, carga_id):
        if CargaModel.find_carga(carga_id):
            return {"message": "Type vehicle id '{}' already exists.".format(carga_id)}, 400 #Bad Request

        dados = Carga.atributos.parse_args()
        carga = CargaModel(**dados)


        """ composição
        if not MotoristaModel.find_by_id(dados['site_id']):
            return {'message': 'The hotel must be associated to a valid site id.'}, 400
        """
        try:
            carga.save_carga()
        except:
            #todo; cnh  =  unique.
            return {"message": "An error ocurred trying to create data vehicle."}, 500 #Internal Server Error
        return carga.json(), 201

    @jwt_required
    def delete(self, carga_id):
        carga = CargaModel.find_carga(carga_id)
        if carga:
            carga.delete_carga()
            return {'message': 'Type vehicle deleted.'}
        return {'message': 'Type vehicle not found.'}, 404