"""
PROGRAMA PRINCIPAL "SERVICIO STREAMING"

El programa ejecuta la funcuion principal main()
Se imprime el menú de opciones del menu principal mediante la funcion MOSTAR_MENU()
Pide al usuario elegir una opcion
Cada opcion realiza una funcion especifica del menú llamando a sus respectivas funciones
En caso de que la opcion ingresada no forme parte del menú, pide vover a ingresar la opcion

"""
import Agregar_producto, Eliminar_producto, Mostrar_catalogo, Cargar_catalogo, Guardar_catalogo, Buscar_producto
# importamos los archivos que contienen los modulos que se ocuparan


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


def main():
    hay_catalogo = False
    salir = False
    while not salir:
        opcion = MOSTRAR_MENU() # muestra el menu y guarda la opcion

        if opcion == 1:
            if hay_catalogo:
                Agregar_producto.agregar_producto(lista_peliculas,lista_series, lista_documentales, lista_eventos_en_vivo)   # Llama a la función de agregar producto del archivo Agregar_producto.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 2:
            if hay_catalogo:
                Buscar_producto.buscar_producto(lista_peliculas,lista_series, lista_documentales, lista_eventos_en_vivo) # Llama a la función de buscar producto del archivo Buscar_producto.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 3:
            if hay_catalogo:
                Eliminar_producto.eliminar_producto(lista_peliculas,lista_series, lista_documentales, lista_eventos_en_vivo) # Llama a la función de eliminar producto del archivo Eliminar_producto.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 4:
            if hay_catalogo:
                Mostrar_catalogo.mostrar_catalogo(lista_peliculas,lista_series, lista_documentales, lista_eventos_en_vivo) # Llama a la función de mostrar catálogo del archivo Mostrar_catalogo.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 5: # Llama a la función de cargar catálogo del archivo Cargar_catalogo.py y guarda las listas
            hay_catalogo, lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo = Cargar_catalogo.cargar_catalogo()
            hay_catalogo = True # verdadero si hay catalogo

        elif opcion == 6:
            if hay_catalogo:
                Guardar_catalogo.guardar_catalogo(lista_peliculas,lista_series, lista_documentales, lista_eventos_en_vivo) # Llama a la función de guardar catálogo del archivo Guardar_catalogo.py
            else:
                print('\nAún no has cargado el catálogo') # Mensaje de error si no se ha cargado el catálogo

        elif opcion == 7:
            salir = True # sale del bucle y finaliza el programa

        else:
            print('La opción no es válida, intenta de nuevo') # Mensaje de error si se elige una opcion invalida

    print('¡Hasta luego!') # mensaje de despedida



main() #se ejecuta el modulo principal
