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
cursor=conexao.cursor()

# comando sql
sql='DELETE FROM pessoas WHERE idpessoa=%s'

# solicitando os dados
idpessoa=input('insira o id registrado que sera excluido: ')

# metodo execute
cursor.execute(sql,idpessoa)

# guardando mudanças
conexao.commit()

# contando a quantidade de registros eliminados
registro_eliminado = cursor.rowcount

# mostrando mensagem ao usuario
print(f'registros eliminados: {registro_eliminado}')

# enxerar conexão
cursor.close()
conexao.close()