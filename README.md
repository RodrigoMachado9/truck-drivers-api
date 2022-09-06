----------------------------
# SERVICE API'S - TRUCK DRIVERS
----------------------------


<p align="center">
    <img 
align="center" 
alt="" height="300" width="850" src="https://media.istockphoto.com/photos/gold-truck-in-black-background-3d-rendering-picture-id1166912511?k=20&m=1166912511&s=170667a&w=0&h=XkjTzWEe5HWODL5KdteLo_QBfe3BxVmCXa0-tCA90J4="/>
</p>


   The purpose of this API will be to improve the truck driver's experience when using certain services.
The services controlled by this API consist of:
user registration, login, logout, drivers registration, vehicle registration, allocation of a certain type of vehicle, allocation of loads, allocation of a certain location, transportation of loads, consultation of truck drivers without load, consultation of truck drivers with their own vehicle , consultation of truck drivers without load to return to their point of origin, consultation of available truck drivers, consultation of the top truck drivers.

----------------------------
## Instructions
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
## Rules
----------------------------
The project contains a bank/example with a specific user configured, however to use the API, it will be necessary to register a specific user, as shown in the example below:

__Endpoint:__ http://127.0.0.1:5000/users/register
__Method__: POST   
Postman settings:


```json

{
   "user": "RodrigoMachado9",
   "password": "5842cadc@9cec#11ec*b44a$4f8d45fa2b75@"
}
```


After registering a particular user, it will be necessary to login; The login endpoint will return a TOKEN to access HTTP services - POST, DELETE & PUT. as example below.


__Endpoint:__ http://127.0.0.1:5000/users/token   
__Method:__ GET   
Postman settings:

```bash

{
    "access token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"
}
```

After generating the post, it will be necessary for the consumption of http services - post, delete, put. As example below:

__Endpoint:__ http://127.0.0.1:5000/drivers/1   
__Method:__ GET    
Postman settings:

```bash
{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
{
	"driver_id": 1,
        "name": "Fulano",
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

__Endpoint:__ http://127.0.0.1:5000/divers/without-shipments
__Method:__ GET   
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            

{
    "driver_without_shipments": [
        {
            "name": "Fulano",
            "sex": "M",
            "rg": "5151805151",
            "origin": null
        }
    ]
}
```


__Endpoint:__ http://127.0.0.1:5000/drivers/own-vehicles
__Method:__ GET   
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            

{
    "truck_drivers_with_own_vehicle": [
        {
            "total": 2
        }
    ]
}
```


__Endpoint:__ http://127.0.0.1:5000/drivers/location
__Method:__ GET   
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            

{
    "truck_drivers_origin_destination": [
        {
            "name": "Rodrigo Machado",
            "origin": "São Paulo",
            "destination": "Florianopolis",
            "modal": "terrestre"
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/drivers/availables
__Method:__ GET   
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            

{

    "available_truck_drivers": [
        {
            "name": "Fulano",
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

__Endpoint:__ http://127.0.0.1:5000/drivers/top-drivers
__Method:__ GET   
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            

{

    "top_truckers": [
        {
            "name": "Fulano",
            "evaluation": "9.0"
        },
	{
            "name": "Other Fulano",
            "evaluation": "9.0"
        }
    ]

}
```


__Endpoint:__ http://127.0.0.1:5000/drivers   
__Method:__ GET   
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}

{

    "truck_drivers": [
        {
            "driver_id": 1007,
            "name": "Fulano",
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
            "driver_id": 1008,
            "name": "Other Fulano",
            "age": 24,
            "rg": "5151805151",
            "org_issuer": "SSP",
            "issuance_date": "06.05.2000",
            "birth_date": "06.05.1995",
            "sex": "M",
            "cnh": "5555",
            "cnh_category": "C",
            "own_vehicle": "true",
            "vehicles": [
                {
                    "veicle_id": 2,
                    "brand": "ferrari",
                    "plate": "5151-4WF",
                    "year": "2019",
                    "color": "vermelha",
                    "body_type": "aberto",
                    "pallets_number": "10",
                    "cubage_meters": "5",
                    "truck_has_tracker": "true",
                    "tracker_type": "mega",
                    "driver_id": 1008,
                    "vehicle_type": [
                        {
                            "vehicle_type_id": 2,
                            "document": "DACTE",
                            "modal": "terrestre",
                            "minimum_shipping": 50,
                            "maximum_shipping": 600,
                            "measurement": "Kg",
                            "total_axles": "5",
                            "vehicle_id": 2
                        }
                    ],
                    "vehicle_status": [
                        {
                            "status_id": 2,
                            "vehicle_has_shipment": "false",
                            "shipping_weight": "400",
                            "vehicle_id": 2
                        }
                    ]
                }
            ],
            "load_location": [
                {
                    "load_location_id": 1,
                    "adress": "Rua do ator",
                    "city": "São Paulo",
                    "evaluation": "9.0",
                    "latitude": "60",
                    "longitude": "58",
                    "origin": "São Paulo",
                    "destination": "Florianopolis",
                    "driver_id": 2,
                    "transport": [
                        {
                            "transport_id": 1,
                            "freight": "10.5",
                            "incident": "chuva forte e via lenta",
                            "arrival": "2019-07-11",
                            "shipments": [
                                {
                                    "shipment_id": 1,
                                    "category": "pesada",
                                    "flammable": "true"
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


__Endpoint:__ http://127.0.0.1:5000/shipments   
__Método:__: GET
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}


{
    "shipments": [
        {
            "shipment_id": 1,
            "category": "pesada",
            "flammable": "true"
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/shipments/transports
__Método:__: GET
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            
{

    "transport": [
        {
            "transport_id": 1,
            "freight": "10.5",
            "incident": "chuva forte e via lenta",
            "shipments": [
                {
                    "shipment_id": 1,
                    "category": "pesada",
                    "flammable": "true"
                }
            ]
        }
    ]

}
```

__Endpoint:__ http://127.0.0.1:5000/shipments/locations
__Método:__: GET
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            

```
```json
{
    "load_location": [
        {
            "location_id": 1,
            "address": "Rua do ator",
            "city": "São Paulo",
            "evaluation": "9.0",
            "latitude": "60",
            "longitude": "58",
            "origin": "São Paulo",
            "destination": "Florianopolis",
            "driver_id": 2,
            "transport": [
                {
                    "transport_id": 1,
                    "freight": "10.5",
                    "incident": "chuva forte e via lenta",
                    "arrival": "2019-07-11",
                    "shipments": [
                        {
                            "shipment_id": 1,
                            "category": "pesada",
                            "flammable": "true"
                        }
                    ]
                }
            ]
        }
    ]
}
```
__Endpoint:__ http://127.0.0.1:5000/vehicles/status   
__Método:__: GET
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            

```
```json
{
    "vehicle_status": [
        {
            "status_id": 1,
            "vehicle_has_shipment": "true",
            "shipping_weight": "400",
            "vehicle_id": 1
        }
    ]
}
```

__Endpoint:__ http://127.0.0.1:5000/vehicles/types
__Método:__: GET
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            

{
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
        },
        {
            "vehicle_type_id": 2,
            "document": "DACTE",
            "modal": "terrestre",
            "minimum_shipping": 50,
            "maximum_shipping": 600,
            "measurement": "Kg",
            "total_axles": "5",
            "vehicle_id": 2
        }
    ]
}
```


__Endpoint:__ http://127.0.0.1:5000/users   
__Método:__: GET
Postman settings:

```bash
{ "Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"}
            

{
    "users": [
        {
            "id": 1,
            "user": "RodrigoMachado9"
        }
    ]
}
```





