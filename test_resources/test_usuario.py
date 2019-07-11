# -*- coding: utf-8 -*-

__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__credits__ = ["Python is life"]
__maintainer__ = "RodrigoMachado9"
__email__ = ["rodrigo.machado3.14@hotmail.com", "https://www.linkedin.com/in/rodrigo-machado-6b0b33177"]

import json
import requests

"""
    INSTRUÇÕES: 
        Os metodo estão comentados, para a realização dos testes, remova o hashtag -> # , 
            para realização de determinado teste.
            No momento os outros testes estão disponiveis via: Postman  no seguinte endereço: 
            https://web.postman.co/collections/7849675-0608a179-5123-440b-be44-650d306f2d16?version=latest&workspace=62969b1d-03de-4c26-8a0b-16583e22ef62#7598f3bb-ccd9-4b62-8be4-074177fd70b1
            após acessar a url, será necessário aalterar a opção: cUrl default para -> python requests;
        :Divirtam-se :)
"""


#todo; raiz dos endpoint's
URL = 'http://127.0.0.1:5000'

def post_login(**kwargs):
    print(kwargs)
    endpoint_cadastro = URL + '/login'
    body_cadastro = {
        'login': kwargs['login'],
        'senha': kwargs['senha']
    }
    headers_cadastro = {
        'Content-Type': 'application/json'
    }

    resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)
    #print(resposta_cadastro.status_code)
    token = resposta_cadastro.json()
    return token['access token']


def post_logout(**kwargs):
    #todo' será necessário realizar o login
    # para retornar o token e consequentemente autorizar o logout'.

    endpoint_cadastro = URL + '/logout'
    body_cadastro = {
        'login': kwargs['login'],
        'senha': kwargs['senha']
    }
    headers_cadastro = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {str(post_login(**kwargs))}'

    }
    resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)
    #print(resposta_cadastro.status_code)
    return print(resposta_cadastro.json())



def post_cadastro(**kwargs):
    endpoint_cadastro = URL + '/cadastro'
    body_cadastro = {
        'login': kwargs['login'],
        'senha': kwargs['senha']
    }
    headers_cadastro = {
        'Content-Type': 'application/json'
    }
    resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)
    assert resposta_cadastro.status_code != '201', 'teste no passed'
    return print(resposta_cadastro.json())

#melhorar metodo com @wrapper
def get_usuario(*args):
    try:
        endpoint_usuario = URL + f"/usuarios{'/' + str(args[0]) if args is not None or str(args) != '' else ''}"
        print(endpoint_usuario)
        aux_get_usuario(endpoint_usuario)
    except:
        endpoint_usuario = URL + "/usuarios"
        aux_get_usuario(endpoint_usuario)

def aux_get_usuario(endpoint_usuario):
    print(endpoint_usuario)
    headers_usuario = {
        'Content-Type': 'application/json'
    }
    resposta_hotel_id = requests.request('GET', endpoint_usuario, headers=headers_usuario)
    print(resposta_hotel_id.status_code)
    print(resposta_hotel_id.json())




def delete_usuario():
    endpoint_usuario = URL + '/usuarios/1'

    headers_usuario = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {str(post_login())}'
    }

    resposta_hotel_id = requests.request('DELETE', endpoint_usuario, headers=headers_usuario)

    print(resposta_hotel_id.status_code)


"""
    metodo responsavel por realizar determinado cadastro
    
"""
#todo. relizar cadastro.
#post_cadastro(login='HelloWorld', senha='python')

"""
    metodo responsavel por realizar determinado login
"""
#todo. realizar login
#post_login(login='TRUCK', senha='is life')

"""
    metodo responsavel por realizar determinado logout
"""
#todo. realizar logout
#post_logout(login='TRUCK', senha='is life')


"""
    Para filtrar determinado usuario, bastanta passar como argumento o (ID) do mesmo,
    caso contrário o método retornará uma lista com todos os usuários
    Exemplos: get_usuario()
              get_usuario(1)
"""
#get_usuario(1)
