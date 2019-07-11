__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

from sql_alchemy import banco


#todo; modelo da minha classe hotel
class UserModel(banco.Model):
    __tablename__ = 'usuarios'

    user_id = banco.Column(banco.Integer, primary_key = True) #todo;  id dinamico
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    #todo função que retornar o meu objeto em formato json !
    def json(self):
        return {
            'user_id':self.user_id,
            'login':self.login
        }

    @classmethod
    def find_user(cls, user_id):
        #todo cls -> é  mesmo que chamar a classe
        # query, consulta o banco
        user = cls.query.filter_by(user_id=user_id).first() # SELECT * FROM usuario WHERE usuario_id = usuario_id LIMIT 1
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        # todo cls -> é  mesmo que chamar a classe
        # query, consulta o banco
        user = cls.query.filter_by(login=login).first()  # SELECT * FROM usuario WHERE usuario_id = usuario_id LIMIT 1
        if user:
            return user
        return None


    def save_user(self):
        banco.session.add(self)
        banco.session.commit()


    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()