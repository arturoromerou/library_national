from psycopg2 import connect, Error
from logger import write_errors

class ConnectionDB:
    
    bd = None
    cursor = None

    def __init__(self, **param):
        try:
            self.db = connect(
                host=param['host'],
                user=param['user'],
                password=param['password']
            )
            self.cursor = self.db.cursor()
        except Error as e:
            write_errors(e, 'Ocurrio un error al conectarse a la base de datos')