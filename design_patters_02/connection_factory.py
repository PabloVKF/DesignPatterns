import mysql.connector


class ConnectionFactory:
    @staticmethod
    def get_connection():
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password='banana123',
            database='empresa'
        )

        return connection
