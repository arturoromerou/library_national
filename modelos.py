from psycopg2 import connect, Error
from logger import write_errors

###### DATABASE CONNECTION #####
class ConnectionDB:

    db = None
    cursor = None

    def __init__(self, **param):
        try:
            self.db = connect(
                host=param['host'],
                user=param['user'],
                password=param['password']
            )
            self.cursor()
        except Error as e:
            write_errors(e, 'Ocurrio un error al conectarse a la base de datos')