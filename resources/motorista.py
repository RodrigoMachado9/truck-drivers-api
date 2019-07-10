from flask_restful import Resource, reqparse
from models.motorista import MotoristaModel
from resources.filtros import normalize_path_params, consulta_com_carga, consulta_sem_carga
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

class Motoristas(Resource):

    def get(self):
        #todo;  retornando uma lista de objetos.
        return {'Motoristas':[motorista.json() for motorista in MotoristaModel.query.all()]}


class Motorista(Resource):

    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('idade')
    atributos.add_argument('rg')
    atributos.add_argument('orgaoemissor')
    atributos.add_argument('dataemissao')
    atributos.add_argument('datanascimento')
    atributos.add_argument('sexo')
    atributos.add_argument('cnh', type=int, required=True, help="The field 'cnh' cannot be left blank.")
    atributos.add_argument('cnhcategoria', required=True, help="The field 'cnhcategoria' cannot be left blank.")
    atributos.add_argument('possueveiculoproprio', required=True, help="The field 'possueveiculoproprio' cannot be left blank.")

    def get(self, motorista_id):
        motorista = MotoristaModel.find_motorista(motorista_id)
        if motorista:
            return motorista.json()
        return {'message': 'Motorista not found.'}, 404

    @jwt_required
    def post(self, motorista_id):
        if MotoristaModel.find_motorista(motorista_id):
            return {"message": "Motorista id '{}' already exists.".format(motorista_id)}, 400 #Bad Request

        dados = Motorista.atributos.parse_args()
        motorista = MotoristaModel(**dados)

        try:
            motorista.save_motorista()
        except:
            #todo; cnh  =  unique.
            return {"message": "An error ocurred trying to create motorista."}, 500 #Internal Server Error
        return motorista.json(), 201

    @jwt_required
    def put(self, motorista_id):
        dados = Motorista.atributos.parse_args()
        motorista = MotoristaModel(**dados) #todo; recebe os atributos da minha tabela.

        motorista_encontrado = MotoristaModel.find_motorista(motorista_id)
        if motorista_encontrado:
            motorista_encontrado.update_motorista(**dados)
            motorista_encontrado.save_motorista()
            return motorista_encontrado.json(), 200
        motorista.save_motorista()
        return motorista.json(), 201

    @jwt_required
    def delete(self, motorista_id):
        motorista = MotoristaModel.find_motorista(motorista_id)
        if motorista:
            motorista.delete_motorista()
            return {'message': 'Motorista deleted.'}
        return {'message': 'Motorista not found.'}, 404