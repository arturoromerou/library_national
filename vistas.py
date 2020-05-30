import os
import sys
from modelos import ConnectionDB
from controladores import EditorialController


# class VistaPrestamos:

#     @staticmethod
#     def menu():
#         os.system("clear")
#         continuar = True
#         while continuar:
#             print("*******************************************")
#             print("             Seccion Prestamos")
#             print("*******************************************\n")
#             print('[1] Registrar prestamo')
#             print('[2] Ver prestamos')
#             print('[3] Eliminar resgisto del sistema')
#             print("\n*******************************************\n")
#             print('[m] Menu Principal')
#             print('[s] Salir \n')
#             opcion = input("ELIJA UNA OPCION: ")
            
#             if opcion == "1":
#                 Vista()
#             elif opcion == "2":
#                 Vista()
#             elif opcion == "3":
#                 Vista()
#             elif opcion == "s":
#                 sys.exit()
#             else:
#                 os.system("clear")
#                 continuar = False


# class VistaUsuarios:
    
#     @staticmethod
#     def menu():
#         os.system("clear")
#         continuar = True
#         while continuar:
#             print("*******************************************")
#             print("              Seccion Usuarios")
#             print("*******************************************\n")
#             print('[1] Agregar Usuarios al sistema')
#             print('[2] Ver Usuarios en el sistema')
#             print('[3] Eliminar Usuarios de sistema')
#             print("\n******************************************\n")
#             print('[m] Menu Principal')
#             print('[s] Salir\n')
#             opcion = input('ELIJA UNA OPCION: ')

#             if opcion == "1":
#                 VistaLibros()
#             elif opcion == "2":
#                 VistaUsuarios()
#             elif opcion == "3":
#                 VistaPrestamos()
#             elif opcion == "s":
#                 sys.exit()
#             else:
#                 os.system("clear")
#                 continuar = False


# class VistaLibros:

#     @staticmethod
#     def menu():
#         os.system("clear")
#         continuar = True
#         while continuar:
#             print("*******************************************")
#             print("               Seccion Libros")
#             print("*******************************************\n")
#             print('[1] Agregar Libros a la base de datos')
#             print('[2] Ver Libros en la base de datos')
#             print('[3] Modificar Libros en la base de datos')
#             print('[4] Eliminar Libros de la base de datos')
#             print("\n****************************************\n")
#             print('[m] Menu Principal')
#             print('[s] Salir\n')
#             opcion = input('ELIJA UNA OPCION: ')

#             if opcion == "1":
#                 VistaLibros.new_book()
#                 os.system("clear")
#             elif opcion == "2":
#                 VistaUsuarios()
#             elif opcion == "3":
#                 VistaPrestamos()
#             elif opcion == "s":
#                 sys.exit()
#             else:
#                 os.system("clear")
#                 continuar = False
    
#     @staticmethod
#     def new_book():
#         if ControladorAutor.autor is None:
#             author = input("Ingresa el Autor: ")
#         ControladorAutor.agregar_autor(
#             {
#             'author': author
#             }
#         )
#         print(ControladorAutor.autor)


class VistaEditorial:

    mensaje = None

    @classmethod
    def create_view(cls):
        name = input('Escriba el nombre de la editorial: ')
        result = EditorialController.create(name=name)
        if result:
            cls.mensaje = "Has registrado la editorial " + result.name
        cls.menu()

    @classmethod
    def list_view(cls):
        for i in EditorialController.read():
            print(f"Editorial: {i[1]}\n")

    @classmethod
    def menu(cls):
        os.system("clear")
        if cls.mensaje:
            print(cls.mensaje)
        continuar = True
        while continuar:
            print("*******************************************")
            print("               Seccion Editorial")
            print("*******************************************\n")
            print('[1] Agregar Editorial')
            print('[2] Ver Editorial')
            print('[3] Modificar Editorial')
            print('[4] Eliminar Editorial')
            print("\n****************************************\n")
            print('[m] Menu Principal')
            print('[s] Salir\n')
            opcion = input('ELIJA UNA OPCION: ')

            if opcion == "1":
                os.system("clear")
                cls.create_view()
            elif opcion == "2":
                os.system("clear")
                cls.list_view()
            #elif opcion == "3":
            #    os.system("clear")
            #    update_view()
            #elif opcion == "4":
            #    os.system("clear")
            #    delete_view()
            elif opcion == "s":
                sys.exit()
            else:
                os.system("clear")
                continuar = False
            opcion = input("Escriba el nombre del Editorial: ")


class VistaAplicacion():

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
            print("[4] Seccion de Editorial")            
            print("\n***************************************************\n")
            print("[s] Salir del sistema\n")
            opcion = input('ELIJA UNA OPCION: ')

            #if opcion == "1":
            #    VistaLibros.menu()
            #elif opcion == "2":
            #    VistaUsuarios.menu()
            #elif opcion == "3":
            #    VistaPrestamos.menu()
            if opcion == "4":
                VistaEditorial.menu()
            elif opcion == "s":
                sys.exit()
            else:
                continuar = False
