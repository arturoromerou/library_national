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
                password=param['password'],
                database=param['database']
            )
            self.cursor = self.db.cursor()
        except Error as e:
            write_errors(e, 'Ocurrio un error al conectarse a la base de datos')

###### EJECUTAR CODIGO SQL ######
    def _ejecutar_sql(
           self, sentencia_sql, param=None, 
           escribir_en_db=True
       ):
           try:
               self.cursor.execute(sentencia_sql, param) # execute corre las sentencias sql
               if escribir_en_db:
                   self.db.commit()
           except Exception as e:
                write_errors(e, f"Ocurrio un error al ejecutar la sentencia SQL:\n\n{sentencia_sql}\n")
           if escribir_en_db:
                   self.db.rollback()

###### CREAR TABLAS ######
    def crear_tabla(self):  
           self._ejecutar_sql(
               """
               CREATE TABLE libros(
                   id_book SERIAL,
                   title_id INT,
                   status INT,
                   editorial_id INT,
                   author_id INT,
                   PRIMARY KEY (id_book)
               )
               """
           )


