#importando o modelo
from models import Pessoas, Usuarios

#criando uma função, um método para inserir; Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Pedro', idade='45')
    print(pessoa)
    pessoa.save() #chamando o método da própria classe


#criando uma função, um método de consulta; realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

#criando função, alteração; altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.idade = 25
    pessoa.save()

#criando função exclusão; exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Assumpção').first()          #para excluir, preciso consulta a pessoa
    pessoa.delete()


#criando método para inserir um novo usuario
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

#criando método consulta todos usuarios
def colsulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__': #criando 'main', para chamar o insere, ou consulta
    insere_usuario('rafael', '1234')
    insere_usuario('galleani', '321')
    colsulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
