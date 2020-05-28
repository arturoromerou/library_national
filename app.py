from modelos import ConnectionDB
def main():
    conexion_pg = ConnectionDB(
        host = '127.0.0.1', # localhost
        user = 'postgres',  # usuario de la bd
        password = 'Ar2098urd',  # contrasenia
        database = 'biblioteca_nacional'  # nombre de la bd
    )

main()