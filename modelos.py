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

################ EJECUTAR CODIGO SQL ################
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

################ CREAR TABLAS ################
    def crear_tabla(self):
        
        ##### TABLA LIBROS #####
        self._ejecutar_sql(
            """
            CREATE TABLE libros(
                id_book INT NOT NULL,
                title_id INT NOT NULL,
                status INT,
                editorial_id INT NOT NULL,
                author_id INT NOT NULL,
                PRIMARY KEY (id_book)
            )
            """
        )
           
        ##### TABLA PRESTAMOS #####
        self._ejecutar_sql(
            """
            CREATE TABLE loans(
                id SERIAL,
                retal_date INT,
                return_date INT,
                id_book INT,
                status INT,
                user_id INT NOT NULL,
                PRIMARY KEY (id)
            )
            """
        )

        ##### TABLA USUARIOS #####
        self._ejecutar_sql(
            """
            CREATE TABLE user(
                user_id SERIAL,
                name VARCHAR(50) NOT NULL,
                dni INT NOT NULL,
                PRIMARY KEY (user_id)
            )
            """
        )

        ##### TABLA EDITORIAL #####
        self._ejecutar_sql(
            """
            CREATE TABLE editorial(
                editorial_id SERIAL,
                editorial VARCHAR(50) NOT NULL,
                PRIMARY KEY (editorial_id)
            )
            """
        )

        ##### TABLA TITULO #####
        self._ejecutar_sql(
            """
            CREATE TABLE title(
                title_id SERIAL,
                title VARCHAR NOT NULL,
                PRIMARY KEY (editorial_id)
            )
            """
        )

        ##### TABLA AUTOR #####
        self._ejecutar_sql(
            """
            CREATE TABLE author(
                author_id SERIAL,
                author VARCHAR(50) NOT NULL,
                PRIMARY KEY (editorial_id)
            )
            """
        )


