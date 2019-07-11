----------------------------
# Objetivo do projeto - tkpd-api caminhoneiros
----------------------------
   O objetivo desta API será melhorar a experiência do caminhoneiro sobre a utilização de determinados serviços.
Os serviços controlados por esta API consistem em:
cadastro de usuario, login, logout, cadastro de motoristas, cadastro de veiculos, alocação de um determinado tipo de veiculo,  alocação de cargas, alocaço de um determinado local, transporte de cargas, consulta de caminhoneiros sem carga,consulta de caminhoneiros com veiculo proprio,consulta de caminhoneiros sem carga para retornar ao seu ponto origem,consulta caminhoneiros disponiveis,  consulta dos top caminhoneiros.

----------------------------
## Instruções sobre o projeto
----------------------------
### primeiro passo: instalação e criação da conta no postman

Os testes referente aos endpoints foram construidos no `POSTMAN` contemplando todos os métodos `HTTP`.
Portanto será necessário criar uma conta nos`POSTMAN`para melhor aproveitamento da `API`. 
Seguindo o caminho `URL` abaixo,  você terá acesso as `COLLECTIONS` deste projeto.

`URL Postman:`
https://web.postman.co/collections/7849675-0608a179-5123-440b-be44-650d306f2d16?version=latest&workspace=62969b1d-03de-4c26-8a0b-16583e22ef62#7598f3bb-ccd9-4b62-8be4-074177fd70b1

Ao acessar a`COLLECTION REST API TKPD` você terá acesso a documentação completa do projeto.

### segundo passo: SO & IDE

A IDE utilizada para o desenvolvimento deste projeto foi o pycharm, entretanto você poderá utilizar a IDE de sua preferencia. 
url para o download, pycharm para SO Ubuntu: https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PCC

### terceiro passo: Git clone 
realize o git clone do projeto 

### quarto passo: requiremens.txt
Na raiz do projeto instale as depedencias da API via terminal, conforme comando abaixo:
```bash
 pip install requirements.txt
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

```bash
http://127.0.0.1:5000/cadastro

configuraçes postman:
Headers -> campo KEY: Content-Type, VALUE: application/json
Body -> raw -> Json
```
```json
{
   "login": "TRUCK",
   "senha": "is life"
}
```


Após o cadastro de um determinado usuário, será necessário realizar o login; O endpoint login retornará um TOKEN de acesso aos serviços HTTP - POST, DELETE & PUT. conforme exemplo abaixo.


```bash
Endpoint:
http://127.0.0.1:5000/login

Configuraçes do postman:
Headers -> campo KEY: Content-Type, VALUE: application/json
Body -> raw -> Json

```
```json
{
    "access token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to"
}
```

Apos gerar o post, o mesmo será necessário para o consumo dos serviços http - post, delete, put. Conforme exemplo abaixo:


```bash
Endpoint:
http://127.0.0.1:5000/motorista/1

Configuraçes do postman:
Headers:{ KEY: Content-Type, Authorization:{Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI4NjYxMTksIm5iZiI6MTU2Mjg2NjExOSwianRpIjoiNjViZDE2YTMtODMwZS00YmVlLTg3NWYtOGY1N2VjMGEwZGNlIiwiZXhwIjoxNTYyODY3MDE5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mH1SoPbevZV0R2V1mg9vlfA_x9QkhlCe60t-Oyt07to}
         VALUE: application/json }
            
Body[raw, Json]

```
```json
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
