#instalado via terminal...o flask e o flask-restful...com isso também, gerar meu requirements, como está no git hub...quem baixar verá o que é necessário instalar para dependÊncias

#agora montar iniciar o nosso desenvolvimento, nosso flask:

from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades              #importando o models pessoas e atividades
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#Se validar, login e senha...autenticar
USUARIOS = {
    'rafael': '1234',                                 #CHAVE -> LOGIN, VALOR -> A SENHA
    'galleani': '321',
    'felipe': '1234'
}

@auth.verify_password                       #decorador não é função....não precisa dos parenteses
#criando método de verificação
def verificacao(login, senha):
    if not (login, senha):                  #se não for informado login e nem a senha
        return False
    return USUARIOS.get(login) == senha

#criando minha primeira classe, minha modelagem -> pessoas e atividades
#criando minha api rest de pessoas
class Pessoa(Resource):
    @auth.login_required                                         #informando qual método precisa passar pela verificação de denha, para acessar esse método é obrigado estar logado
    def get(self, nome):                                         #criando o método get, nome como parametro
        pessoa = Pessoas.query.filter_by(nome=nome).first()      #first para poder pegar o objeto
        #tratando erro, com try e except
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada!'
            }
        return response
#criado o método GET
#Criando o método POST, método de alteração

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()   #para receber o objeto
        #alterar os dados, post manda os dados pela repocição
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response ={
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

#Criando o método Delete
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluída com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status': 'sucesso','mensagem': mensagem}

#Criando uma classe para listar tudo e inserir pessoas
class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas] #uma lista de dicionário antes era uma lista de objetos
        return response

    # para inserir
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

#Criando a classe Atividades
class ListaAtividade(Resource): #trazer a lista e permitir uma inclusão
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome}  for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/') #registrando a rota
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividade, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)





