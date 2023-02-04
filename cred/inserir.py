# importacion del modulo
import psycopg2

#conexao a base de dados
conexao=psycopg2.connect(user='postgres',
                          password='1234',
                          #a senha deve ser alterada e colocada a que estao utilizando no sgbd
                          host='localhost',
                          port='5432',
                          database='testebd')
                          #e o nome do data base deve ser igual ao que esta aqui para que de certo

# utilizar cursor
cursor = conexao.cursor()

# criando sequencia sql
sql='INSERT INTO pessoas (nome,sobrenome,idade) VALUES(%s,%s,%s)'

# solicitando os dados
nome=input('insira o nome: ')
sobrenome=input('insira o sobenome: ')
idade=input('insira a idade: ')

# dados = uma tupla com os dados na sequencia apresentada
dados=(nome,sobrenome,idade)

# fazendo uso do metodo execute 
cursor.execute(sql,dados)

# guardar registro
conexao.commit()

# registro inserido
registros=cursor.rowcount

# mostrar resultado
print(f'registro inserido: {registros}')

# enxerar conexão
cursor.close()
conexao.close()