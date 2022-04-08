from distutils.log import debug
from flask import Flask, render_template
import re

# https://stackoverflow.com/questions/59474572/flask-404ing-on-static-content-i-have-in-an-assets-directory
STATIC_FOLDER = 'templates/assets'
app = Flask(__name__,
            static_folder=STATIC_FOLDER)

# criar a primeira pagina do site
# route --> teste.com/contatos -- caminho apos o nome do dominio
# funcao --> o que você quer exibir naquela pagina
# template


class Usuario:
    def __init__(self, usuario, email, senha):
        self.set_usuario(usuario)
        self.set_email(email)
        self.__set_senha(senha)

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        if self.__validar_usuario(usuario):
            self.usuario = usuario
        else:
            print("Erro ao adicionar usuario")

    def get_email(self):
        return self.email

    def set_email(self, email):
        if self.__validar_email(email):
            self.email = email
        else:
            print("Erro ao adicionar e-mail")

    def __validar_usuario(self, usuario):
        if len(usuario) > 0 and usuario != "":
            return True
        else:
            return False

    def __validar_email(self, email):
        # https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            return True
        else:
            return False

    def get_senha(self):
        return self.__senha

    def __set_senha(self, senha):
        if len(senha) >= 8:
            self.__senha = senha
        else:
            print("Senha muito fraca")


class Login:
    def __init__(self, usuario):
        self.usuario = usuario

    def login(self):
        try:
            achou = False
            for x in list_usuarios:
                if x.get_usuario() == self.usuario.get_usuario() and x.get_senha() == self.usuario.get_senha():
                    achou = True
                    break

            if achou == True:
                print("Tudo certinho^^")
            else:
                print("Usuario ou senha invalidos")

        except ValueError:
            print('Erro. O valor informado não é inteiro')


list_usuarios = []

"""

user = Usuario("Admin", "contato@teste.com", "12345678")
list_usuarios.append(user)

user2 = Usuario("Admin2", "contato2@teste.com", "1234567")
list_usuarios.append(user2)

user3 = Usuario("Admin3", "contato3@teste.com", "123456")
list_usuarios.append(user3)

login1 = Login(Usuario("Admin2", "asd@gmail.com", "12345678"))
login1.login()

"""


@app.route('/')
def homepage():
    return render_template("index.html", titulo="Home")


@app.route('/login')
def login():
    return render_template("login.html", titulo="Login")


@app.route('/usuarios')
def usuarios():
    if len(list_usuarios) > 0:
        string = '<ul>\n'
        for x in list_usuarios:
            string = string + \
            f"   <li>Usuario: {x.get_usuario()} | E-mail: {x.get_email()} </li>\n"
        string = string + "</ul>\n"
    else:
        return "Lista está vazia"
  




app.run(debug=True)
if __name__ == '__main__':  # IF esse arquivo foi rodado direto,
    # não foi chamado como biblioteca
    #app.run(host='localhost', port=5002, debug=True)
    app.run(debug=True)
    # suba um servidor, na porta 5002,
    # configuração de debug
    # debug: salvar dá reload


# servidor do heroku
# pip install gunicorn
# gerar pip freeze > requirements.txt
