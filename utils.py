#importando o modelo
from models import Pessoas

#criando uma função, um método para inserir; Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Assumpção', idade='35')
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
    pessoa = Pessoas.query.filter_by(nome='Assumpção').first()
    pessoa.nome = 'Francisco'
    pessoa.save()

#criando função exclusão; exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Francisco').first()          #para excluir, preciso consulta a pessoa
    pessoa.delete()


if __name__ == '__main__': #criando 'main', para chamar o insere, ou consulta
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()
