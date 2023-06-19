
import Agregar_producto, Eliminar_producto, Mostrar_catalogo, Cargar_catalogo, Guardar_catalogo, Buscar_producto
# importamos los archivoa que contienen los modulos que se ocuparan


def MOSTRAR_MENU():
    # menú principal
    print('Menú Principal')
    print()
    print('1. Agregar un producto')
    print('2. Buscar producto')
    print('3. Eliminar Producto')
    print('4. Mostrar catálogo')
    print('5. Cargar catálogo')
    print('6. Guardar catálogo')
    print('7. Salir')
    print()
    opcion = int(input('Elige una opción: ')) #solicita al usuario que elija una opcion
    return opcion


def Elegir_opcion(hay_catalogo, catalogo):
    salir = False
    while not salir:
        opcion = MOSTRAR_MENU() # muestra el menu y guarda la opcion

        if opcion == 1:
            if hay_catalogo:
                Agregar_producto.agregar_producto(catalogo)   # Llama a la función de agregar producto del archivo Agregar_producto.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 2:
            if hay_catalogo:
                Buscar_producto.buscar_producto() # Llama a la función de buscar producto del archivo Buscar_producto.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 3:
            if hay_catalogo:
                Eliminar_producto.eliminar_producto() # Llama a la función de eliminar producto del archivo Eliminar_producto.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 4:
            if hay_catalogo:
                Mostrar_catalogo.mostrar_catalogo() # Llama a la función de mostrar catálogo del archivo Mostrar_catalogo.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 5:
            catalogo = Cargar_catalogo.cargar_catalogo() # Llama a la función de cargar catálogo del archivo Cargar_catalogo.py
            hay_catalogo = True # guarda si hay catalogo

        elif opcion == 6:
            if hay_catalogo:
                Guardar_catalogo.guardar_catalogo() # Llama a la función de guardar catálogo del archivo Guardar_catalogo.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 7:
            salir = True # sale del bucle y finaliza el programa

        else:
            print('La opción no es válida, intenta de nuevo') # Mensaje de error si se elige una opcion invalida

    print('¡Hasta luego!') # mensaje de despedida


hay_catalogo = False # indica que no hay catalogo para iniciar la seleccion del menu
catalogo = []
Elegir_opcion(hay_catalogo, catalogo) #se ejecuta el modulo principal