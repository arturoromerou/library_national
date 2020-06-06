"""App models.""" 
from psycopg2 import connect, Error
from logger import write_errors


class ConnectionDB:
    """Connection class."""
    
    bd = None
    cursor = None

    def __init__(self, **param):
        """Connection constructor."""
        try:
            self.db = connect(
                host = '127.0.0.1', # localhost
                user = 'postgres',  # usuario de la bd
                password = '/1(Iwasborn)*84',  # contrasenia
                database = 'biblioteca_nacional'  # nombre de la bd
            )
            self.cursor = self.db.cursor()
        except Error as e:
            write_errors(e, 'Ocurrio un error al conectarse a la base de datos')

    def ejecutar_sql(
        self, 
        sentencia_sql, 
        param=None, 
        escribir_en_db=True
    ):
        """Ejecuta codigo SQL."""
        try:
            execute = self.cursor.execute(sentencia_sql, param) # execute corre las sentencias sql
            if escribir_en_db:
                result =  self.db.commit()
            return self.cursor.rowcount    # numero de filas afectadas
        except Exception as e:
            write_errors(e, f"Ocurrio un error al ejecutar la sentencia SQL:\n\n{sentencia_sql}\n")
            if escribir_en_db:
                self.db.rollback()


    def leer_desde_sql(self, sql_code):
        """Leer codigo sql."""
        registros = None

        self.ejecutar_sql(sql_code, escribir_en_db=False)
        try:
            registros = self.cursor.fetchall()
        except Exception as e:
            write_errors(e, f'Un error ocurrió al momento de leer desde la BD')
        return registros


class Tabla(ConnectionDB):
    """Crear tablas."""

    def crear_tabla(self):
        
        # TABLA LIBROS
        self.ejecutar_sql(
            """
            CREATE TABLE IF NOT EXISTS books(
                id_book INT NOT NULL,
                title VARCHAR(255) NOT NULL,
                status INT,
                editorial_id INT NOT NULL,
                author_id INT NOT NULL,
                PRIMARY KEY (id_book)
            )
            """
        )
           
        # TABLA PRESTAMOS
        self.ejecutar_sql(
            """
            CREATE TABLE IF NOT EXISTS rent(
                id SERIAL,
                start_date DATE,
                end_date DATE,
                id_book INT,
                user_id INT NOT NULL,
                PRIMARY KEY (id)
            )
            """
        )

        # TABLA USUARIOS
        self.ejecutar_sql(
            """
            CREATE TABLE IF NOT EXISTS "user"(
                user_id SERIAL,
                name VARCHAR(50) NOT NULL,
                dni INT NOT NULL,
                PRIMARY KEY (user_id)
            )
            """
        )

        # TABLA EDITORIAL
        self.ejecutar_sql(
            """
            CREATE TABLE IF NOT EXISTS editorial(
                editorial_id SERIAL,
                name VARCHAR(50) NOT NULL,
                PRIMARY KEY (editorial_id)
            )
            """
        )

        # TABLA AUTOR
        self.ejecutar_sql(
            """
            CREATE TABLE IF NOT EXISTS author(
                author_id SERIAL,
                name VARCHAR(50) NOT NULL,
                PRIMARY KEY (author_id)
            )
            """
        )


class Model():
    """Generic model class."""

    table_name = None  # nombre de la tabla 
    connection = ConnectionDB()  # Esto no se hace

    def create(self):
        """Guarda en base de datos."""
        table_name = self.table_name # le asignamos el valor del olbjeto self
        keys = ", ".join(self.__dict__.keys()) 
        values_placeholders = ", ".join(["%s" for i in range(len(self.__dict__.keys()))]) # 
        values = self.__dict__.values()
        sql = f"INSERT INTO {table_name} ({keys}) VALUES ({values_placeholders})"
        
        return self.connection.ejecutar_sql(sql, tuple(values)) # retorna el numero de fila afectadas

    @classmethod
    def read(cls):
        """Obtiene un elemento de la base de datos."""
        table_name = cls.table_name
        sql = f"SELECT * FROM {table_name}"
        
        return cls.connection.leer_desde_sql(sql)

    def update(self):
        """Actualiza un elemento de la base de datos."""
        table_name = self.table_name
        sql = f"UPDATE {table_name} SET id = %s"
        
        self.connection(sql)

    def delete(self):
        """Borra un elemento de la base de datos."""
        table_name = self.table_name
        sql = f"DELETE FROM {table_name} WHERE editorial_id = %d"
        
        self.connection.ejecutar_sql(sql)

class Editorial(Model):
    """Clase Editorial."""

    table_name = "editorial"
    name = None
    editorial_id = None

    def __init__(self, name):
        """Método constructor."""
        self.name = name

    # Comenté (Miguel)
    """
    def eliminar(self, editorial_id):
        self.editorial_id   
    """   

class Autor(Model):
    """Clase Autor"""

    table_name = "author"

    name = None

    mobile_id = None

    def __init__(self, name):
        """Metodo Constructor"""
        self.name = name

class Libro(Model):
    """Clase Libro"""
    
    table_name = "books"
    title = None
    author_id = None
    editorial_id = None
    status = None

    def __init__(self, title, author_id, editorial_id, status):
        """Metodo Constructor"""
        self.title = title
        self.author_id = author_id
        self.editorial_id = editorial_id
        self.status = status


# TODO: Terminar este modelo
class Usuario(Model):
    """Clase usuario."""

    pass


# TODO: Terminar este modelo
class Rent(Model):
    """Clase alquiler."""

    pass