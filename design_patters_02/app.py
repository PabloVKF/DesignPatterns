from connection_factory import ConnectionFactory


connection = ConnectionFactory.get_connection()

cursor = connection.cursor()

cursor.execute('SELECT * FROM tb_departamento')

for linha in cursor:
    print(linha)

connection.close()
