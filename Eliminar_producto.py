
def eliminar_producto(lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo):
    """
    se reciben  las listas de cada categoria para hacer la busqueda y eliminar el producto:
    lista_peliculas
    lista_series
    lista_documentales
    lista_eventos_en_vivo

    Realiza la busqueda por lista y por cada elemento en ella
    Imprime el contenido del producto y su ubicacion

    """
    Existe_producto = False #Mientras Existe_producto es falso se repite el bucle
    while not Existe_producto:
        # solicitar al usuario que introduzca las palabras clave para buscar el producto
        clave_busqueda = str(input("Ingrese las palabras clave del título del producto: ")) #Recibe las palabras claves para la busqueda
        listas = lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo  #Se agrupan las listas para darles porcicion
        for lista in listas: # La busqueda se realiza en todas las listas
            for linea in lista: #la busqueda se realiza en cada elemento de la lista
                if clave_busqueda.lower() in linea.lower(): #Analiza si la clave esta contenida en cada elemento de la lista
                    lista.remove(linea) #se elimina la linea/producto
                    Existe_producto = True #variable verdadera para dar salida al bucle
                    print("Producto Eliminado:")  # mensaje de exito

        if not Existe_producto:
            print('El producto no existe, intenta de nuevo') # si no se encuentra el producto, se manda mensaje de error y se invita a intentar de nuevo