from flask_restful import Resource, reqparse
from models.transporte import TransporteModel
from flask_jwt_extended import jwt_required
import sqlite3

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

        try:
            transporte.save_transporte()
        except:
            #todo; cnh  =  unique.
            return {"message": "An error ocurred trying to create data transporte."}, 500 #Internal Server Error
        return transporte.json(), 201

    @jwt_required
    def delete(self, transporte_id):
        transporte = TransporteModel.find_transporte(transporte_id)
        if transporte:
            transporte.delete_transporte()
            return {'message': 'Type transporte deleted.'}
        return {'message': 'Type transporte not found.'}, 404