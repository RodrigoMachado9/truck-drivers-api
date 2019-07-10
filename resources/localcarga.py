from flask_restful import Resource, reqparse
from models.local_carga import LocalCargaModel
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

class LocalCargas(Resource):

    def get(self):
        #todo;  retornando uma lista de objetos.
        return {'local_cargas':[lcarga.json() for lcarga in LocalCargaModel.query.all()]}


class LocalCarga(Resource):

    atributos = reqparse.RequestParser()
    atributos.add_argument('endereco', type=str, required=True, help="The field 'endereco' cannot be left blank.")
    atributos.add_argument('cidade')
    atributos.add_argument('avaliacao')
    atributos.add_argument('latitude')
    atributos.add_argument('longitude')
    atributos.add_argument('origem')
    atributos.add_argument('destino')
    atributos.add_argument('motorista_id', type=int, required=True, help="Every localcarga needs to be linked motorista.")



    def get(self, local_carga_id):
        localcarga = LocalCargaModel.find_local_carga(local_carga_id)
        if localcarga:
            return localcarga.json()
        return {'message': 'carga not found.'}, 404

    @jwt_required
    def post(self, local_carga_id):
        if LocalCargaModel.find_local_carga(local_carga_id):
            return {"message": "Type local_carga id '{}' already exists.".format(local_carga_id)}, 400 #Bad Request

        dados = LocalCarga.atributos.parse_args()
        localcarga = LocalCargaModel(**dados)

        """ composição
        if not MotoristaModel.find_by_id(dados['site_id']):
            return {'message': 'The hotel must be associated to a valid site id.'}, 400
        """
        try:
            localcarga.save_local_carga()
        except:
            #todo; cnh  =  unique.
            return {"message": "An error ocurred trying to create data local_carga."}, 500 #Internal Server Error
        return localcarga.json(), 201

    @jwt_required
    def delete(self, local_carga_id):
        localcarga = LocalCargaModel.find_tipo_veiculo(local_carga_id)
        if localcarga:
            localcarga.delete_local_carga()
            return {'message': 'Type local_carga deleted.'}
        return {'message': 'Type local_carga not found.'}, 404