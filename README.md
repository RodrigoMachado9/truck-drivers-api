----------------------------
# Objetivo do projeto - tkpd-api caminhoneiros
----------------------------
   O objetivo desta API será melhorar a experiência do caminhoneiro sobre a utilização de determinados serviços.
Os serviços controlados por esta API consistem em:
cadastro de usuario, login, logout, cadastro de motoristas, cadastro de veiculos, alocação de um determinado tipo de veiculo,  alocação de cargas, alocação de um determinado local, transporte de cargas, consulta de caminhoneiros sem carga,consulta de caminhoneiros com veiculo proprio,consulta de caminhoneiros sem carga para retornar ao seu ponto origem,consulta de caminhoneiros disponiveis,  consulta dos top caminhoneiros.

----------------------------
## Instruções sobre o projeto
----------------------------
### primeiro passo: instalação e criação da conta no postman

Os testes referente aos endpoints foram construidos no `POSTMAN` contemplando todos os métodos `HTTP`.
Portanto será necessário criar uma conta no`POSTMAN`para o melhor aproveitamento da `API`. 
Seguindo o caminho `URL` abaixo,  você terá acesso as `COLLECTIONS` deste projeto.

`URL Postman:`
https://web.postman.co/collections/7849675-0608a179-5123-440b-be44-650d306f2d16?version=latest&workspace=62969b1d-03de-4c26-8a0b-16583e22ef62#7598f3bb-ccd9-4b62-8be4-074177fd70b1

Ao acessar a`COLLECTION REST API TKPD` você terá acesso a documentação completa do projeto.

### segundo passo: SO & IDE

A IDE utilizada para o desenvolvimento deste projeto foi o pycharm, entretanto você poderá utilizar a IDE de sua preferencia. 
url para o download, pycharm/Ubuntu: https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PCC

### terceiro passo: Git clone 
realize o git clone do projeto 

### quarto passo: requiremens.txt
Na raiz do projeto instale as depedencias da API via terminal, conforme comando abaixo:
```bash
 pip install -r requirements.txt
```
### quinto passo: configurando variáveis
Abra o terminal e digite os comandos abaixo.
```bash
 export FLASK_APP=app
 export FLASK_ENV=Development
 export FLASK_DEBUG=True

```
### sexto passo: start app 
Na raiz do projeto execute o comando abaixo, para subir a aplicação.
```bash
 python app.py
```
### sétimo passo: abra o Postman para o consumo dos endpoints, conforme documentação do projeto.
`URL Postman:`
https://web.postman.co/collections/7849675-0608a179-5123-440b-be44-650d306f2d16?version=latest&workspace=62969b1d-03de-4c26-8a0b-16583e22ef62#7598f3bb-ccd9-4b62-8be4-074177fd70b1

----------------------------
## Regras para a utilização da api
----------------------------
O projeto contem um banco/exemplo com um determinado usuario configurado, entretando para a utilização da API, será necessário cadastrar um determinado usuário,  Conforme exemplo abaixo:

__Endpoint:__ http://127.0.0.1:5000/cadastro   
__Método:__ POST   
Configuraçes do postman:   

```json
Headers -> campo KEY: Content-Type, VALUE: application/json
Body -> raw -> Json

{
   "login": "python",
   "senha": "islife"
}
```


Após o cadastro de um determinado usuário, será necessário realizar o login; O endpoint login retornará um TOKEN de acesso aos serviços HTTP - POST, DELETE & PUT. conforme exemplo abaixo.


__Endpoint:__ http://127.0.0.1:5000/login   
__Método:__ GET   
Configuraçes do postman:    
```json
Headers -> campo KEY: Content-Type, VALUE: application/json
Body -> raw -> Json

{
    "access token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"
}
```

Após gerar o post, o mesmo será necessário para o consumo dos serviços http - post, delete, put. Conforme exemplo abaixo:

__Endpoint:__ http://127.0.0.1:5000/motorista/1   
__Método:__ GET    
Configuraçes do postman:   

```json
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:
{
   "nome": "Fulano",
	"idade": 25,
	"rg": "5151805151",
	"orgaoemissor": "SSP",
	"dataemissao": "06.05.2000",
	"datanascimento": "06.05.1995",
	"sexo": "M",
	"cnh": "66666666",
	"cnhcategoria": "C",
	"possueveiculoproprio":"true"
}
```

---
## Endpoints
---

__Endpoint:__ http://127.0.0.1:5000/motoristas/local_carga/motoristas_sem_carga   
__Método:__ GET   
Configuraçes do postman:   
```json
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]


Body:
{
    "motoristas_sem_carga": [
        {
            "nome": "Fernando",
            "sexo": "M",
            "rg": "5151805151",
            "origem": null
        }
    ]
}
```


__Endpoint:__ http://127.0.0.1:5000/motoristas/motoristas_com_veiculo_proprio   
__Método:__ GET   
Configuraçes do postman:    
```json
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:
{
    "caminhoneiros_com_veiculo_proprio": [
        {
            "total": 2
        }
    ]
}
```


__Endpoint:__ http://127.0.0.1:5000/motoristas/local_carga/veiculo/origem_destino   
__Método:__ GET   
Configuraçes do postman:  

```json
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:{
    "caminhoneiros_origem_destino": [
        {
            "nome": "Fulano",
            "origem": "São Paulo",
            "destino": "Florianopolis",
            "modal": "terrestre"
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/motoristas/status_veiculo/motoristas_disponiveis   
__Método:__ GET   
Configuraçes do postman:
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:{

    "caminhoneiros_disponiveis": [
        {
            "nome": "Fulano",
            "sexo": "M",
            "idade": 25,
            "cnhcategoria": "C",
            "marca": "ferrari",
            "tipo_de_carroceria": "aberto",
            "rastreador": "true",
            "modal": "terrestre",
            "cargamin": 50,
            "cargamax": 600
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/motoristas/top_motoristas   
__Método:__ GET   
Configuraçes do postman:
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:{

    "top_caminhoneiros": [
        {
            "nome": "Fernando",
            "avaliacao": "9.0"
        }
    ]

}
```


__Endpoint:__ http://127.0.0.1:5000/motoristas   
__Método:__ GET   
Configuraçes do postman:
```json
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]


Body:{

    "Motoristas": [
        {
            "motorista_id": 1,
            "nome": "Fernando",
            "idade": 25,
            "rg": "5151805151",
            "orgao_emissor": "SSP",
            "data_emissao": "06.05.2000",
            "data_nascimento": "06.05.1994",
            "sexo": "M",
            "cnh": "7777777",
            "cnh_categoria": "C",
            "possue_veiculo_proprio": "true",
            "veiculos": [
                {
                    "veiculo_id": 1,
                    "marca": "mercedes",
                    "placa": "5151-4WF",
                    "ano": "2018",
                    "cor": "amarelo",
                    "tipo_de_carroceria": "aberto/grande_baixa",
                    "numero_de_pallets": "10",
                    "cubagem_em_metros": "5",
                    "caminhao_possue_rastreador": "true",
                    "tipo_do_rastreador": "mega",
                    "motorista_id": 1,
                    "tipo_do_veiculo": [
                        {
                            "tipo_veiculo_id": 1,
                            "documento": "DACTE",
                            "modal": "terrestre",
                            "carga_minima": 50,
                            "carga_maxima": 600,
                            "unidade_de_medida": "Kg",
                            "total_de_eixos": "5",
                            "veiculo_id": 1
                        }
                    ],
                    "status_do_veiculo": [
                        {
                            "status_id": 1,
                            "veiculo_carregado": "true",
                            "peso_da_carga": "400",
                            "veiculo_id": 1
                        }
                    ]
                }
            ],
            "localcarga": []
        },
        {
            "motorista_id": 2,
            "nome": "Fulano",
            "idade": 24,
            "rg": "5151805151",
            "orgao_emissor": "SSP",
            "data_emissao": "06.05.2000",
            "data_nascimento": "06.05.1995",
            "sexo": "M",
            "cnh": "5555",
            "cnh_categoria": "C",
            "possue_veiculo_proprio": "true",
            "veiculos": [
                {
                    "veiculo_id": 2,
                    "marca": "ferrari",
                    "placa": "5151-4WF",
                    "ano": "2019",
                    "cor": "vermelha",
                    "tipo_de_carroceria": "aberto",
                    "numero_de_pallets": "10",
                    "cubagem_em_metros": "5",
                    "caminhao_possue_rastreador": "true",
                    "tipo_do_rastreador": "mega",
                    "motorista_id": 2,
                    "tipo_do_veiculo": [
                        {
                            "tipo_veiculo_id": 2,
                            "documento": "DACTE",
                            "modal": "terrestre",
                            "carga_minima": 50,
                            "carga_maxima": 600,
                            "unidade_de_medida": "Kg",
                            "total_de_eixos": "5",
                            "veiculo_id": 2
                        }
                    ],
                    "status_do_veiculo": [
                        {
                            "status_id": 2,
                            "veiculo_carregado": "false",
                            "peso_da_carga": "400",
                            "veiculo_id": 2
                        }
                    ]
                }
            ],
            "localcarga": [
                {
                    "local_carga_id": 1,
                    "endereco": "Rua do ator",
                    "cidade": "São Paulo",
                    "avaliacao": "9.0",
                    "latitude": "60",
                    "longitude": "58",
                    "origem": "São Paulo",
                    "destino": "Florianopolis",
                    "motorista_id": 2,
                    "transporte": [
                        {
                            "transporte_id": 1,
                            "frete": "10.5",
                            "incidente": "chuva forte e via lenta",
                            "chegada": "2019-07-11",
                            "carga": [
                                {
                                    "carga_id": 1,
                                    "categoria": "pesada",
                                    "inflamavel": "true"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
}
```


__Endpoint:__ http://127.0.0.1:5000/cargas   
__Método:__ GET   
Configuraçes do postman:
```json
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:{
    "cargas": [
        {
            "carga_id": 1,
            "categoria": "pesada",
            "inflamavel": "true"
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/transportes   
__Método:__ GET   
Configuraçes do postman:  
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:{

    "transportes": [
        {
            "transporte_id": 1,
            "frete": "10.5",
            "incidente": "chuva forte e via lenta",
            "carga": [
                {
                    "carga_id": 1,
                    "categoria": "pesada",
                    "inflamavel": "true"
                }
            ]
        }
    ]

}
```

__Endpoint:__ http://127.0.0.1:5000/local_cargas   
__Método:__ GET   
Configuraçes do postman:
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

```
```json
Body:{
    "local_cargas": [
        {
            "local_carga_id": 1,
            "endereco": "Rua do ator",
            "cidade": "São Paulo",
            "avaliacao": "9.0",
            "latitude": "60",
            "longitude": "58",
            "origem": "São Paulo",
            "destino": "Florianopolis",
            "motorista_id": 2,
            "transporte": [
                {
                    "transporte_id": 1,
                    "frete": "10.5",
                    "incidente": "chuva forte e via lenta",
                    "chegada": "2019-07-11",
                    "carga": [
                        {
                            "carga_id": 1,
                            "categoria": "pesada",
                            "inflamavel": "true"
                        }
                    ]
                }
            ]
        }
    ]
}
```
__Endpoint:__ http://127.0.0.1:5000/status   
__Método:__ GET   
Configuraçes do postman:
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

```
```json
Body:{
    "Status_veiculo": [
        {
            "status_id": 1,
            "veiculo_carregado": "true",
            "peso_da_carga": "400",
            "veiculo_id": 1
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/tipo_veiculos   
__Método:__ GET   
Configuraçes do postman:

```json
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:{
    "tipo_veiculos": [
        {
            "tipo_veiculo_id": 1,
            "documento": "DACTE",
            "modal": "terrestre",
            "carga_minima": 50,
            "carga_maxima": 600,
            "unidade_de_medida": "Kg",
            "total_de_eixos": "5",
            "veiculo_id": 1
        },
        {
            "tipo_veiculo_id": 2,
            "documento": "DACTE",
            "modal": "terrestre",
            "carga_minima": 50,
            "carga_maxima": 600,
            "unidade_de_medida": "Kg",
            "total_de_eixos": "5",
            "veiculo_id": 2
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/status   
__Método:__ GET   
Configuraçes do postman:

```json
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:
    "Status_veiculo": [
        {
            "status_id": 1,
            "veiculo_carregado": "true",
            "peso_da_carga": "400",
            "veiculo_id": 1
        }
    ]
}
```


__Endpoint:__ http://127.0.0.1:5000/usuarios   
__Método:__ GET   
Configuraçes do postman:
```json
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:
   {
    "usuarios": [
        {
            "id": 1,
            "login": "python"
        }
    ]
}
```









