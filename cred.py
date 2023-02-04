import psycopg2

#conectando a base de datos
conexao=psycopg2.connect(user='postgres',
                          password='226913',
                          #a senha deve ser alterada e colocada a que estao utilizando no sgbd
                          host='localhost',
                          port='5432',
                          database='testebd')
                          #e o nome do data base deve ser igual ao que esta aqui para que de certo

cursor=conexao.cursor()
#executando a conexao

#inserir informacao
comando = 'INSERT INTO ' + '''nome da tabela(a ordem das informacoes que vc vai inseriri)''' 'VALUE'#(os valores que vc quer inseriri)

cursor.execute(comando)
conexao.commit()#editar o banco de dados
resultado = cursor.fetchall() #ler o banco de dados




cursor.close()
conexao.close()