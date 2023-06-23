
def buscar_producto(lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo):
    """
    se reciben  las listas de cada categoria para hacer la busqueda:
    lista_peliculas
    lista_series
    lista_documentales
    lista_eventos_en_vivo

    Realiza la busqueda por lista y por cada elemento en ella
    Imprime el contenido del producto y su ubicacion

    """
    Existe_producto = False #variable para indicar si existe el producto
    while not Existe_producto: #Mientras Existe_producto es falso se repite el bucle
        clave_busqueda = str(input("Ingrese las palabras clave del título del producto: ")) #Recibe las palabras claves para la busqueda
        listas = lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo #Se agrupan las listas para darles porcicion
        ubicacon = None #Declara ubicacion como vacia
        for lista in listas: # La busqueda se realiza en todas las listas
            for linea in lista: #la busqueda se realiza en cada elemento de la lista
                if clave_busqueda.lower() in linea.lower(): #Analiza si la clave esta contenida en cada elemento de la lista
                    print(linea)   #Imprime la linea/producto
                    Existe_producto = True #variable verdadera para dar salida al bucle
                    ubicacon = listas.index(lista) # Identifica la lista que se analiza con su posicion en listas

                                        # Imprime la categoria donde se encuentra dependiendo la ubicacion
                    if ubicacon == 0:
                        print('El producto se encuentra en la categoria: Peliculas')
                    elif ubicacon == 1:
                        print('El producto se encuentra en la categoria: Series')
                    elif ubicacon == 2:
                        print('El producto se encuentra en la categoria: Documentales')
                    elif ubicacon == 3:
                        print('El producto se encuentra en la categoria: Eventos deportivos en vivo')


        if not Existe_producto: # si no se encuentra el producto, se manda mensaje de error y se invita a intentar de nuevo
            print('El producto no existe, intenta de nuevo')