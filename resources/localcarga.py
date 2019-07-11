__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

from flask_restful import Resource, reqparse
from models.local_carga import LocalCargaModel
from flask_jwt_extended import jwt_required
import sqlite3


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
        return {'message': 'local_carga not found.'}, 404

    @jwt_required
    def post(self, local_carga_id):
        if LocalCargaModel.find_local_carga(local_carga_id):
            return {"message": "Type local_carga id '{}' already exists.".format(local_carga_id)}, 400 #Bad Request

        dados = LocalCarga.atributos.parse_args()
        localcarga = LocalCargaModel(**dados)


        try:
            localcarga.save_local_carga()
        except:
            #todo; cnh  =  unique.
            return {"message": "An error ocurred trying to create data local_carga."}, 500 #Internal Server Error
        return localcarga.json(), 201

    @jwt_required
    def delete(self, local_carga_id):
        localcarga = LocalCargaModel.find_local_carga(local_carga_id)
        if localcarga:
            localcarga.delete_local_carga()
            return {'message': 'Type local_carga deleted.'}
        return {'message': 'Type local_carga not found.'}, 404