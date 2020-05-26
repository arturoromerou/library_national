import os


def menu_administrador():
    os.system("clear")
    continuar = True
    while continuar:
        print("\n**************** LIBRERIA NACIONAL ****************\n")
        print('[1] Agregar Libros a la base de datos')
        print('[2] Ver Libros en la base de datos')
        print('[3] Modificar Libros en la base de datos')
        print('[4] Eliminar Libros de la base de datos')
        print("\n**************** PRESTAMOS ****************\n")
        print('[5] Registar Entregas y Prestamos a Usuarios')
        print('[6] Ver Prestamos y Entregas a Usuarios')
        print("\n**************** USUARIOS ****************\n")
        print('[7] Agregar Usuarios al sistema')
        print('[8] Ver Usuarios en el sistema')
        print('[9] Eliminar Usuarios de sistema')
        print("\n*******************************************\n")
        print('\n[s] Salir del sistema\n')
        opcion = input('DIGITE SU SLECCION: ')
        

        if opcion == "1":
            agregar_articulos_almacen()
        elif opcion == "2":
            ver_articulos()
        elif opcion == "3":
            modificar_articulo_almacen()
        elif opcion == "4":
            eliminar_articulo()
        elif opcion == "s":
            sys.exit()
        else:
            opcion == input("elija una seleccion valida: ")
menu_administrador()