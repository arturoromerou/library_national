import os
import sys

class VistaPrestamos:

    @staticmethod
    def menu():
        os.system("clear")
        continuar = True
        while continuar:
            print("************* Seccion Prestamos *************\n")
            print('[1] Registrar prestamo')
            print('[2] Ver prestamos')
            print('[3] Eliminar resgisto del sistema')
            print("\n*******************************************\n")
            print('[m] Menu Principal')
            print('[s] Salir \n')
            opcion = input("ELIJA UNA OPCION: ")
            
            if opcion == "1":
                Vista()
            elif opcion == "2":
                Vista()
            elif opcion == "3":
                Vista()
            elif opcion == "s":
                sys.exit()
            else:
                continuar = False

class VistaUsuarios:
    
    @staticmethod
    def menu():
        os.system("clear")
        continuar = True
        while continuar:
            print("************* Seccion Usuarios *************\n")
            print('[1] Agregar Usuarios al sistema')
            print('[2] Ver Usuarios en el sistema')
            print('[3] Eliminar Usuarios de sistema')
            print("\n******************************************\n")
            print('[m] Menu Principal')
            print('[s] Salir\n')
            opcion = input('ELIJA UNA OPCION: ')

            if opcion == "1":
                VistaLibros.()
            elif opcion == "2":
                VistaUsuarios.()
            elif opcion == "3":
                VistaPrestamos.()
            elif opcion == "s":
                sys.exit()
            else:
                continuar = False

class VistaLibros:

    @staticmethod
    def menu():
        os.system("clear")
        continuar = True
        while continuar:
            print("************* Seccion Libros *************\n")
            print('[1] Agregar Libros a la base de datos')
            print('[2] Ver Libros en la base de datos')
            print('[3] Modificar Libros en la base de datos')
            print('[4] Eliminar Libros de la base de datos')
            print("\n****************************************\n")
            print('[m] Menu Principal')
            print('[s] Salir\n')
            opcion = input('ELIJA UNA OPCION: ')

            if opcion == "1":
                VistaLibros.()
            elif opcion == "2":
                VistaUsuarios.()
            elif opcion == "3":
                VistaPrestamos.()
            elif opcion == "s":
                sys.exit()
            else:
                continuar = False

class VistaAplicacion:

    @staticmethod
    def iniciar():
        os.system("clear")
        VistaAplicacion.bienvenida()
        VistaAplicacion.menu()

    @staticmethod
    def bienvenida():
        print("Bienvenid@ al Menu Principal de la Libreria Nacional...!")

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print("\n***************************************************")
            print("               LIBRERIA NACIONAL                 ")
            print("***************************************************\n")
            print("[1] Seccion de Libros")
            print("[2] Seccion de Usuarios")
            print("[3] Seccion de Prestamos")            
            print("\n***************************************************\n")
            print("[s] Salir del sistema\n")
            opcion = input('ELIJA UNA OPCION: ')

            if opcion == "1":
                VistaLibros.menu()
            elif opcion == "2":
                VistaUsuarios.menu()
            elif opcion == "3":
                VistaPrestamos.menu()
            elif opcion == "s":
                sys.exit()
            else:
                opcion == input("elija una seleccion valida: ")
