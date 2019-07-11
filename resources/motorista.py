__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

from flask_restful import Resource, reqparse
from models.motorista import MotoristaModel
from resources.filtros import motorista_sem_carga, caminhoneiro_possue_veiculo_proprio, listagem_origem_destino, top_caminhoneiros, caminhoneiro_disponivel
from flask_jwt_extended import jwt_required
import sqlite3


class CaminhoneirosDisponiveis(Resource):
    """
    Mostrar somentes determinados caminhoneiros disponiveis
    """

    def get(self):
        connection = sqlite3.connect('case_truck.db')
        cursor = connection.cursor()

        # todo; top caminhoneiros
        resultado = cursor.execute(caminhoneiro_disponivel)

        caminhoneiros = []
        for linha in resultado:
            caminhoneiros.append({
                'nome': linha[0],
                'sexo': linha[1],
                'idade': linha[2],
                'cnhcategoria': linha[3],
                'marca': linha[4],
                'tipo_de_carroceria': linha[5],
                'rastreador': linha[6],
                'modal': linha[7],
                'cargamin': linha[8],
                'cargamax': linha[9]
            })

        return {'caminhoneiros_disponiveis': caminhoneiros}




class CaminhoneiroAvaliacao(Resource):
    """
    Mostrar os top 10 caminhoneiros.
    """
    def get(self):
        connection = sqlite3.connect('case_truck.db')
        cursor = connection.cursor()

        # todo; top caminhoneiros
        resultado = cursor.execute(top_caminhoneiros)

        caminhoneiros = []
        for linha in resultado:
            caminhoneiros.append({
                'nome': linha[0],
                'avaliacao': linha[1]
            })

        if caminhoneiros[0]['avaliacao'] in (['10','10.0']):
            return {'top_10':caminhoneiros}

        return {'top_caminhoneiros': caminhoneiros}


class CaminhoneirosOrigemDestino(Resource):
    """
    Mostrar uma lista de origem e destino agrupado por cada um dos tipos.
    """
    def get(self):
        connection = sqlite3.connect('case_truck.db')
        cursor = connection.cursor()

        #todo; hehe
        resultado = cursor.execute(listagem_origem_destino)

        caminhoneiros = []
        for linha in resultado:
            caminhoneiros.append({
            'nome': linha[0],
            'origem': linha[1],
            'destino': linha[2],
            'modal': linha[3]
            })

        return {'caminhoneiros_origem_destino': caminhoneiros}



class CaminhoneirosVeiculoProprio(Resource):
    """
    Precisamos saber quantos caminhoneiros tem veiculo próprio.
    """
    def get(self):
        connection = sqlite3.connect('case_truck.db')
        cursor = connection.cursor()

        #todo; hehe
        resultado = cursor.execute(caminhoneiro_possue_veiculo_proprio)

        caminhoneiros = []
        for linha in resultado:
            caminhoneiros.append({
            'total': linha[0]
            })

        return {'caminhoneiros_com_veiculo_proprio': caminhoneiros}


class MotoristasLocalCarga(Resource):
    """
    Precisamos de um método para consultar todos os motoristas
    que não tem carga para voltar ao seu destino de origem
    """
    def get(self):
        connection = sqlite3.connect('case_truck.db')
        cursor = connection.cursor()

        #todo; hehe
        resultado = cursor.execute(motorista_sem_carga)

        motoristas = []
        for linha in resultado:
            motoristas.append({
            'nome': linha[0] ,
            'sexo': linha[1],
            'rg': linha[2],
            'origem': linha[3],
            })
        return {'motoristas_sem_carga': motoristas}


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