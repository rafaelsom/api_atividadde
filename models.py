#models -> onde vai estar as classes que vão referenciar uma tabela do banco de dados

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship     #Responsaveis por criar nossas sessões de banco de dados
from sqlalchemy.ext.declarative import declarative_base     #importando a base declarativa

#criando um sql lite

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)  #convert_unicode=True -> para não ter problemas com acentuação no banco de dados
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property() #trecho necesário para criação do banco de dados, para fazer alterações e consultas também

#criando as tabelas... depois de criar o banco de dados... tabelas são classes

class Pessoas(Base):                        #nome da classe pode ser diferente do nome da tabela
    __tablename__ = 'pessoas'                #nome da tabela
    id = Column(Integer, primary_key=True)  #nossa chave primária
    nome = Column(String(40), index=True)   #index=True -> criando index da coluna, para uma consulta mais rápida
    idade = Column(Integer)

    def __repr__(self):                     #função para imprimir, representação da classe, uma forma de representar o objeto
        return '<Pessoa {}>'.format(self.nome)

    def save(self):         #criando um método para adicionar o próprio objeto
        db_session.add(self)
        db_session.commit()

    def delete(self):   #criando outro método....delete
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))   #chave estrangeira, com o nome da tabela
    pessoa = relationship("Pessoas")                       #nome da classe -> reconhece o relacionamento de pessoas com atividade


    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Usuarios(Base):
    __tablename__ = 'Usuarios'
    id = Column(Integer, primary_key=True)          #id nossa primary key, Intereger, inteiro
    login = Column(String(20), unique=True)         #do tipo Sting e vai ser único -> unique=True -> não aceitar usuario com o mesmo nome
    senha = Column(String(20))

    def __repr__(self):       #criando a UDF, representação
        return '<Usuario {}>'.format(self.login)

    def save(self):            #criando método save também
        db_session.add(self)
        db_session.commit()

    def delete(self):           #criando método delete
        db_session.delete(self)
        db_session.commit()

def init_db():                                              #criando um método, ele que cria o banco de dados
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()