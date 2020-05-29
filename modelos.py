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
    def ejecutar_sql(
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

################ LEER CODIGO SQL ################
    def leer_desde_sql(self):
        try:
            registros = self.cursor.fetchall()
            for x in registros:
                print(x)
        except Exception as e:
            write_errors(e, f'Un error ocurrió al momento de leer desde la BD')
        return registros

################ CREAR TABLAS ################
class Tabla(ConnectionDB):

    def crear_tabla(self):
        
        ##### TABLA LIBROS #####
        self.ejecutar_sql(
            """
            CREATE TABLE books(
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
        self.ejecutar_sql(
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
        self.ejecutar_sql(
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
        self.ejecutar_sql(
            """
            CREATE TABLE editorial(
                editorial_id SERIAL,
                editorial VARCHAR(50) NOT NULL,
                PRIMARY KEY (editorial_id)
            )
            """
        )

        ##### TABLA TITULO #####
        self.ejecutar_sql(
            """
            CREATE TABLE title(
                title_id SERIAL,
                title VARCHAR NOT NULL,
                PRIMARY KEY (editorial_id)
            )
            """
        )

        ##### TABLA AUTOR #####
        self.ejecutar_sql(
            """
            CREATE TABLE author(
                author_id SERIAL,
                author VARCHAR(50) NOT NULL,
                PRIMARY KEY (editorial_id)
            )
            """
        )

################ INSERTAR A LAS TABLAS ################
class Registrar(ConnectionDB):

    def insertar_editorial(self, editorial):
        self.ejecutar_sql(
            """INSERT INTO editorial (editorial) 
            VALUES (%s,)""",
            (editorial)
    )

    def insertar_titulo(self, title):
        self.ejecutar_sql(
            """INSERT INTO title (title) 
            VALUES (%s,)""",
            (title)
    )

    def insertar_autor(self, author):
        self.ejecutar_sql(
            """INSERT INTO author (author) 
            VALUES (%s,)""",
            (author)
    )

    def insertar_usuario(self, name, dni):
        self.ejecutar_sql(
            """INSERT INTO user (name, dni) 
            VALUES (%s, %s)""",
            (name, dni)
        )

################ VER LOS DATOS DE LAS TABLAS ################
class Obtener(ConnectionDB):

    def ver_libros(self):
        self.ejecutar_sql(
            "SELECT * FROM books",
            escribir_en_db=False
        )
        self.leer_desde_sql()

    def ver_usuarios(self):
        self.ejecutar_sql(
            "SELECT * FROM user",
            escribir_en_db=False
        )
        self.leer_desde_sql()

    def ver_prestamos(self):
        self.ejecutar_sql(
            "SELECT * FROM loans",
            escribir_en_db=False
        )
        self.leer_desde_sql()

################ ELIMINAR DATOS DE LAS TABLAS ################
class Eliminar(ConnectionDB):

    def eliminar_libro(self, id_book):
        self.ejecutar_sql(
            "DELETE FROM books WHERE id_book=%s",
            (id_book,)
        )
    
    def eliminar_usuario(self, user_id):
        self.ejecutar_sql(
            "DELETE FROM user WHERE user_id=%s",
            (user_id,)
        )

    def eliminar_registro(self, id):
        self.ejecutar_sql(
            "DELETE FROM loans WHERE id=%s",
            (id)
        )   
