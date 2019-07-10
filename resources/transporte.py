from flask_restful import Resource, reqparse
from models.transporte import TransporteModel
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

class Transportes(Resource):

    def get(self):
        #todo;  retornando uma lista de objetos.
        return {'transportes':[transporte.json() for transporte in TransporteModel.query.all()]}


class Transporte(Resource):

    atributos = reqparse.RequestParser()
    atributos.add_argument('frete')
    atributos.add_argument('incidente')
    atributos.add_argument('local_carga_id', type=int, required=True, help="Every transporte needs to be linked local_carga.")


    def get(self, transporte_id):
        transporte = TransporteModel.find_transporte(transporte_id)
        if transporte:
            return transporte.json()
        return {'message': 'transporte not found.'}, 404

    @jwt_required
    def post(self, transporte_id):
        if TransporteModel.find_transporte(transporte_id):
            return {"message": "Type transporte id '{}' already exists.".format(transporte_id)}, 400 #Bad Request

        dados = Transporte.atributos.parse_args()
        transporte = TransporteModel(**dados)

        """ composição
        if not MotoristaModel.find_by_id(dados['site_id']):
            return {'message': 'The hotel must be associated to a valid site id.'}, 400
        """
        try:
            transporte.save_transporte()
        except:
            #todo; cnh  =  unique.
            return {"message": "An error ocurred trying to create data vehicle."}, 500 #Internal Server Error
        return transporte.json(), 201

    @jwt_required
    def delete(self, transporte_id):
        transporte = TransporteModel.find_transporte(transporte_id)
        if transporte:
            transporte.delete_transporte()
            return {'message': 'Type transporte deleted.'}
        return {'message': 'Type transporte not found.'}, 404