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

# criando sentença sql
sql='UPDATE pessoas SET nome=%s,sobrenome=%s,idade=%s WHERE idpessoa=%s'

# consulta de dados a usuario
idpessoa=input('insira id da pessoa a editar: ')
nome=input('insira nome: ')
sobrenome=input('insira sobrenome: ')
idade=input('insira idade: ')

#recoleccion de dados
dados=(nome,sobrenome,idade,idpessoa)

# utilizando o metodo execute
cursor.execute(sql,dados)

# guardar modificacion
conexao.commit()

#contar el numero de cambios
atualizacoes=cursor.rowcount

# mostrar mensagem ao usuario
print(f'registro actualizado: {actualizacion}')

# enxerar conexão
cursor.close()
conexao.close()

