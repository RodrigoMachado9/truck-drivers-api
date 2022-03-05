----------------------------
# Project objective - truckers tkpd-api
----------------------------
   The purpose of this API will be to improve the truck driver's experience when using certain services.
The services controlled by this API consist of:
user registration, login, logout, drivers registration, vehicle registration, allocation of a certain type of vehicle, allocation of loads, allocation of a certain location, transportation of loads, consultation of truck drivers without load, consultation of truck drivers with their own vehicle , consultation of truck drivers without load to return to their point of origin, consultation of available truck drivers, consultation of the top truck drivers.

----------------------------
## Project instructions
----------------------------
### First step: installation and account creation in postman

   The endpoint tests were built in `POSTMAN` contemplating all `HTTP` methods.
Therefore, it will be necessary to create a `POSTMAN` account for the best use of the `API`.
Following the `URL` path below, you will have access to the `COLLECTIONS` of this project.

`URL Postman:`
https://web.postman.co/collections/7849675-0608a179-5123-440b-be44-650d306f2d16?version=latest&workspace=62969b1d-03de-4c26-8a0b-16583e22ef62#7598f3bb-ccd9-4b62-8be4-074177fd70b1

by accessing the `COLLECTION REST API TKPD` you will have access to the complete documentation of the project.

### Second step: OS and IDE

  The IDE used for the development of this project was pycharm, however you can use the IDE of your choice.
url for download, pycharm/Ubuntu: https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PCC


### Third step: Git Clone 
perform the git clone of the project,
```bash
git clone https://github.com/RodrigoMachado9/tkpd-drivers-api.git
```

### Fourth step: requirements.txt
In the root of the project, install the API dependencies via terminal, according to the command below:
```bash
 pip install -r requirements.txt
```

### Fifth step: setting variables
Open the terminal and type the commands below.
```bash
 export FLASK_APP=app
 export FLASK_ENV=Development
 export FLASK_DEBUG=True

```

### Sixth step: start app 
In the root of the project, execute the command below, to upload the application.
```bash
 python app.py
```

### Seventh step: open Postman to view the endpoints, as per the project documentation.
`URL Postman:`
https://web.postman.co/collections/7849675-0608a179-5123-440b-be44-650d306f2d16?version=latest&workspace=62969b1d-03de-4c26-8a0b-16583e22ef62#7598f3bb-ccd9-4b62-8be4-074177fd70b1



----------------------------
## Rules for using the api
----------------------------
The project contains a bank/example with a specific user configured, however to use the API, it will be necessary to register a specific user, as shown in the example below:

__Endpoint:__ http://127.0.0.1:5000/cadastro   
__Método:__ POST   
Postman settings:

```json
Headers -> field KEY: Content-Type, VALUE: application/json
Body -> raw -> Json

{
   "user": "python",
   "password": "islife"
}
```


After registering a particular user, it will be necessary to login; The login endpoint will return a TOKEN to access HTTP services - POST, DELETE & PUT. as example below.


__Endpoint:__ http://127.0.0.1:5000/login   
__Método:__ GET   
Postman settings:
```bash
Headers -> field KEY: Content-Type, VALUE: application/json
Body -> raw -> Json

{
    "access token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"
}
```

After generating the post, it will be necessary for the consumption of http services - post, delete, put. As example below:

__Endpoint:__ http://127.0.0.1:5000/motorista/1   
__Método:__ GET    
Postman settings:

```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:
{
   "nome": "Fulano",
	"age": 25,
	"rg": "5151805151",
	"org_issuer": "SSP",
	"date_issue": "06.05.2000",
	"birth_date": "06.05.1995",
	"sex": "M",
	"cnh": "66666666",
	"cnh_category": "C",
	"own_vehicle":"true"
}
```

---
## Endpoints
---

__Endpoint:__ http://127.0.0.1:5000/motoristas/local_carga/motoristas_sem_carga   
__Método:__ GET   
Postman settings:
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]


Body:
{
    "driver_without_shipments": [
        {
            "name": "Fernando",
            "sex": "M",
            "rg": "5151805151",
            "origin": null
        }
    ]
}
```


__Endpoint:__ http://127.0.0.1:5000/motoristas/motoristas_com_veiculo_proprio   
__Method:__ GET   
Postman settings:
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:
{
    "truck_drivers_with_own_vehicle": [
        {
            "total": 2
        }
    ]
}
```


__Endpoint:__ http://127.0.0.1:5000/motoristas/local_carga/veiculo/origem_destino   
__Method:__ GET   
Postman settings:

```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:{
    "truck_drivers_origin_destination": [
        {
            "name": "Rodrigo J Machado",
            "origin": "São Paulo",
            "destination": "Florianopolis",
            "modal": "terrestre"
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/motoristas/status_veiculo/motoristas_disponiveis   
__Method:__ GET   
Postman settings:
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:{

    "available_truck_drivers": [
        {
            "name": "Marcos Araujo Sobrinho",
            "sex": "M",
            "age": 25,
            "cnh_category": "C",
            "brand": "ferrari",
            "body_type": "aberto",
            "tracker": "true",
            "modal": "terrestre",
            "minimum_shipping": 50,
            "maximum_shipping": 600
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/motoristas/top_motoristas   
__Method:__ GET   
Postman settings:
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

Body:{

    "top_truckers": [
        {
            "name": "Fernando Souza",
            "avaliacao": "9.0"
        },
	{
            "name": "Marcos Araujo Sobrinho",
            "avaliacao": "9.0"
        }
    ]

}
```


__Endpoint:__ http://127.0.0.1:5000/motoristas   
__Method:__ GET   
Postman settings:
```bash
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]


Body:{

    "truck_drivers": [
        {
            "driver_id": 1007,
            "name": "Marcos Araujo Sobrinho",
            "age": 25,
            "rg": "5151805151",
            "org_issuer": "SSP",
            "issuance_date": "06.05.2000",
            "birth_date": "06.05.1994",
            "sex": "M",
            "cnh": "7777777",
            "cnh_category": "C",
            "own_vehicle": "true",
            "vehicles": [
                {
                    "vehicle_id": 100701,
                    "brand": "mercedes",
                    "plate": "5151-4WF",
                    "year": "2018",
                    "color": "amarelo",
                    "body_type": "aberto/grande_baixa",
                    "pallets_number": "10",
                    "cubage_meters": "5",
                    "truck_has_tracker": "true",
                    "tracker_type": "mega",
                    "driver_id": 1007,
                    "vehicle_type": [
                        {
                            "vehicle_type_id": 1,
                            "document": "DACTE",
                            "modal": "terrestre",
                            "minimum_shipping": 50,
                            "maximum_shipping": 600,
                            "measurement": "Kg",
                            "total_axles": "5",
                            "vehicle_id": 1
                        }
                    ],
                    "vehicle_status": [
                        {
                            "status_id": 100702,
                            "vehicle_has_shipment": "true",
                            "shipping_weight": "400",
                            "vehicle_id": 100701
                        }
                    ]
                }
            ],
            "load_location": []
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
Configuraçôes do postman:
```bash
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
Configuraçôes do postman:  
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
Configuraçôes do postman:
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
Configuraçôes do postman:
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
Configuraçôes do postman:

```bash
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
Configuraçôes do postman:

```bash
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
Configuraçôes do postman:
```bash
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





