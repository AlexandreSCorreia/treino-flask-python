from distutils.log import debug
from flask import Flask, render_template, request, jsonify, redirect, url_for
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
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.set_email(email)
        self.__senha = senha

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

    def set_senha(self, senha):
        self.__senha = senha


class Login:
    def __init__(self, usuario):
        self.usuario = usuario

    def logar(self):
        achou = False
        for x in list_usuarios:
            if x.get_email() == self.usuario.get_email() and x.get_senha() == self.usuario.get_senha():
                achou = True
        return achou


list_usuarios = []

user = Usuario("Admin", "contato@teste.com", "12345678")
list_usuarios.append(user)
print(user.__dict__)
user2 = Usuario("Admin2", "contato2@teste.com", "1234567")
list_usuarios.append(user2)
print(user2.__dict__)
user3 = Usuario("Admin3", "contato3@teste.com", "123456")
list_usuarios.append(user3)
print(user3.__dict__)

"""
login1 = Login(Usuario("", "contato@teste.com", "12345678"))
print(login1.__dict__)
result = login1.logar()
print(result)

"""



@app.route('/')
def homepage():
    return render_template("index.html",  atributos={"titulo": "Home"})


@app.route('/login', methods=['GET', 'POST'])
def logar():
    if request.method == 'GET':
        return render_template("login.html", atributos={"titulo": "Login"})

    if request.method == 'POST':
        if Login(Usuario("", request.form.get('email'), request.form.get('password'))).logar() == True:
            return redirect(url_for('painel'))
        else:
            return render_template("login.html", atributos={"titulo": "Login", "erro": "Usuario ou senha invalidos"})

@app.route('/painel', methods=['GET', 'POST'])
def painel():
    if request.method == 'GET':
        return render_template("painel.html", atributos={"titulo": "Dashboard"})




@app.route('/usuarios')
def usuarios():
    if len(list_usuarios) > 0:
        string = '<ul>\n'
        for x in list_usuarios:
            string = string + \
                f"   <li>Usuario: {x.get_usuario()} | E-mail: {x.get_email()} </li>\n"
        string = string + "</ul>\n"
        return string
    else:
        return "Lista está vazia"


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        """return the information for <user_id>"""

    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.form  # a multidict containing POST data

    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
        return "Deletando informacao haha"
    else:
        # POST Error 405 Method Not Allowed
        data = [doc for doc in {
            "Error": "Algo de errado ocorreu ao tentar deletar!"}]
        return jsonify(isError=True,
                       message="Error",
                       statusCode=405,
                       data=data), 405


if __name__ == '__main__':
    app.run(debug=True)
# servidor do heroku
# pip install gunicorn
# gerar pip freeze > requirements.txt
