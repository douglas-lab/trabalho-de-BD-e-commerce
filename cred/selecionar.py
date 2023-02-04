import psycopg2

#conectando a base de dados
conexao = psycopg2.connect(user='postgres',
                          password='1234',
                          #a senha deve ser alterada e colocada a que estao utilizando no sgbd
                          host='localhost',
                          port='5432',
                          database='testebd')
                          #e o nome do data base deve ser igual ao que esta aqui para que de certo

# utilisando cursor
cursor = conexao.cursor()

#criando sequencia sql
sql = 'SELECT * FROM '

# utilizar metodo execute 
cursor.execute(sql)

# mostrar resultado
resultado = cursor.fetchall()
print(resultado)

# enxerar conexão
cursor.close()
conexao.close()
