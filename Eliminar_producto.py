
def eliminar_producto():
    Existe_producto = False
    while not Existe_producto:
        #solicitar al usuario que introduzca las palabras clave para buscar el producto
        clave_busqueda = str(input("Ingrese las palabras clave del título del producto: "))
        lineas =[] # Lista para almacenar las líneas del archivo

        # Leer todas las líneas del archivo y guardarlas en lineas
        Peliculas = open('Peliculas.txt', 'r')
        lineas = Peliculas.readlines()
        Peliculas.close()
        # buscar en todos los elementos de la lista
        for linea in lineas:
            # se busca las palabras clave en cada linea
            if clave_busqueda.lower() in linea.lower():
                lineas.remove(linea) # Se elimina la línea que contiene el producto
                print("Producto Eliminado:") # mensaje de exito
                Existe_producto = True # el producto se encontro
                Peliculas.close()
                # se actualiza el documento Peliculas.txt con los datos de la lista
                Peliculas = open('Peliculas.txt', 'w')
                Peliculas.writelines(lineas)
                Peliculas.close()

        # Leer todas las líneas del archivo y guardarlas en lineas
        Series = open('Series.txt', 'r')
        lineas = Series.readlines()
        Series.close()
        # buscar en todos los elementos de la lista
        for linea in lineas:
            # se busca las palabras clave en cada linea
            if clave_busqueda.lower() in linea.lower():
                lineas.remove(linea)# Se elimina la línea que contiene el producto
                print("Producto Eliminado:")# mensaje de exito
                Existe_producto = True # el producto se encontro
                Series.close()
                # se actualiza el documento Peliculas.txt con los datos de la lista
                Series = open('Series.txt', 'w')
                Series.writelines(lineas)
                Series.close()

        # Leer todas las líneas del archivo y guardarlas en lineas
        Documentales = open('Documentales.txt', 'r')
        lineas = Documentales.readlines()
        Documentales.close()
        for linea in lineas:
            # se busca las palabras clave en cada linea
            if clave_busqueda.lower() in linea.lower():
                lineas.remove(linea) # Se elimina la línea que contiene el producto
                print("Producto Eliminado:")# mensaje de exito
                Existe_producto = True # el producto se encontro
                Documentales.close()
                # se actualiza el documento Peliculas.txt con los datos de la lista
                Documentales = open('Documentales.txt', 'w')
                Documentales.writelines(lineas)
                Documentales.close()


        # Leer todas las líneas del archivo y guardarlas en lineas
        Eventos_Deportivos = open('Eventos_Deportivos.txt', 'r')
        lineas = Eventos_Deportivos.readlines()
        Eventos_Deportivos.close()
        for linea in lineas:
            # se busca las palabras clave en cada linea
            if clave_busqueda.lower() in linea.lower():
                lineas.remove(linea) # Se elimina la línea que contiene el producto
                print("Producto Eliminado:") # mensaje de exito
                Existe_producto = True # el producto se encontro
                Eventos_Deportivos.close()
                # se actualiza el documento Peliculas.txt con los datos de la lista
                Eventos_Deportivos = open('Eventos_Deportivos.txt', 'w')
                Eventos_Deportivos.writelines(lineas)
                Eventos_Deportivos.close()

    print("Catálogo actualizado correctamente.")