
def agregar_registro(lista, producto):
    """Recibe el producto y una lista donde se agregara el producto"""
    lista.append(producto) #agrega al final de la lista el nuevo producto

def agregar_producto(lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo):
    """Recibe la listas de cada categoria
        Solicita los datos necesarios dependiendo la categooria/tipo de producto, el cual tambien es solictada
        Agrega el producto a la lista correspondiente a su categoria
    """
    Existe_tipo = False
    while not Existe_tipo:  # variable que indica si existe una catagoria
        tipo_producto = input("Ingrese el tipo de producto (Pelicula/Serie/Documental/Evento deportivo en vivo): ")

        if tipo_producto.lower() == "pelicula":    # Solicitar información necesaria de la película
            catalogo = open('catalogo.txt', 'a')
            titulo = input("Ingrese el título del producto: ")
            actor_principal = str(input("Ingrese el actor principal: "))
            director = str(input("Ingrese el director: "))
            año = str(input("Ingrese el año: "))
            costo_renta = str(input("Ingrese el costo de renta: "))
            costo_venta = str(input("Ingrese el costo de venta: "))

            #genera el producto, organizando los datos antes solicitados
            producto = 'Título: ' + titulo + '   Actor principal: ' + actor_principal + '   Director: ' + director + '   Año: ' + año + '   Costo de renta: ' + costo_renta + '   Costo de venta: ' + costo_venta + '\n'

            # funcion para agregar el producto a la lista, como parametros se usan la lista de peliculas y el producto antes generado
            agregar_registro(lista_peliculas, producto)
            Existe_tipo = True # se dechara verdadera la funcion para dar salida al bucle

        elif tipo_producto.lower() == "serie":
            titulo = input("Ingrese el título del producto: ")        # Solicitar información necesaria de la serie
            actor_principal = str(input("Ingrese el actor principal: "))
            director = str(input("Ingrese el director: "))
            temporadas = str(input("Ingrese el número de temporadas: "))
            costo_renta = str(input("Ingrese el costo de renta: "))
            costo_venta = str(input("Ingrese el costo de venta: "))

            # genera el producto, organizando los datos antes solicitados
            producto = 'Título: ' + titulo + '   Actriz o actor principal: ' + actor_principal + '   Directora o director: ' + director + '   Temporadas: ' + temporadas + '   Costo de renta: ' + costo_renta + '   Costo de venta: ' + costo_venta + '\n'

            # funcion para agregar el producto a la lista, como parametros se usan la lista de series y el producto antes generado
            agregar_registro(lista_series, producto)
            Existe_tipo = True # se dechara verdadera la funcion para dar salida al bucle

        elif tipo_producto.lower() == "documental":
            titulo = input("Ingrese el título del producto: ")     # Solicitar información necesaria del documental
            director = str(input("Ingrese el director: "))
            tema = str(input("Ingrese el tema: "))
            año = str(input("Ingrese el año: "))
            costo_renta = str(input("Ingrese el costo de renta: "))
            costo_venta = str(input("Ingrese el costo de venta: "))

            # genera el producto, organizando los datos antes solicitados
            producto = 'Título: ' + titulo + '   Directora o director: ' + director + '   Tema: ' + tema + '   Año: ' + año + '   Costo de renta: ' + costo_renta + '   Costo de venta: ' + costo_venta + '\n'

            # funcion para agregar el producto a la lista, como parametros se usan la lista de documentales y el producto antes generado
            agregar_registro(lista_documentales, producto)
            Existe_tipo = True # se dechara verdadera la funcion para dar salida al bucle

        elif tipo_producto.lower() == "evento deportivo en vivo":
            titulo = input("Ingrese el título del producto: ")          # Solicitar información necesaria del evento
            deporte = str(input("Ingrese el deporte: "))
            fecha = str(input("Ingrese la fecha: "))
            hora = str(input("Ingrese la hora: "))
            lugar = str(input("Ingrese el lugar: "))
            costo_venta = str(input("Ingrese el costo de venta: "))

            # genera el producto, organizando los datos antes solicitados
            producto = 'Título: ' + titulo + '   Deporte: ' + deporte + '   Fecha: ' + fecha + '   Hora: ' + hora + '   Lugar: ' + lugar + '   Costo de venta: ' + costo_venta + '\n'

            # funcion para agregar el producto a la lista, como parametros se usan la lista de eventos y el producto antes generado
            agregar_registro(lista_eventos_en_vivo, producto)
            Existe_tipo = True # se dechara verdadera la funcion para dar salida al bucle

        else:
            # en caso de no encontrar un tipo,se manda mensaje con la leyenda: tipo de producto invalido  y se repite el bucle
            print("Tipo de producto inválido. Intenta de nuevo")

    print("Catálogo actualizado correctamente.")  # mensaje de actualizacion
