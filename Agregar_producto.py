
def agregar_producto(catalogo):
    Existe_tipo = False
    while not Existe_tipo: # variable que indica si existe una catagoria
        tipo_producto = input("Ingrese el tipo de producto (Pelicula/Serie/Documental/Evento deportivo en vivo): ")


        if tipo_producto.lower() == "pelicula":
            # Solicitar información necesaria de la película
            titulo = input("Ingrese el título del producto: ")
            actor_principal = str(input("Ingrese el actor principal: "))
            director = str(input("Ingrese el director: "))
            año = str(input("Ingrese el año: "))
            costo_renta = str(input("Ingrese el costo de renta: "))
            costo_venta = str(input("Ingrese el costo de venta: "))
            # se unen los datos sobre la pelicula en un solo renglon
            # es necesario que los datos anteriores sean del tipo string para poder añadirlos al arcivo
            producto = 'Título: ' + titulo + '   Actor principal: ' + actor_principal + '   Director: ' + director + '   Año: ' + año + '   Costo de renta: ' + costo_renta + '   Costo de venta: ' + costo_venta + '\n'
            Peliculas = open('Peliculas.txt', 'a') # Abrir el archivo Peliculas.txt como escritura para poder agregar al final
            Peliculas.write(producto) # Escribir la información de la película en el archivo
            Peliculas.close() #se cierra el archivo para actualizarlo
            Existe_tipo = True  # existe una categoria
            print("Pelicula agregada correctamente.") # mensaje de exito

        elif tipo_producto.lower() == "serie":
            # Solicitar información necesaria de la película
            titulo = input("Ingrese el título del producto: ")
            actor_principal = str(input("Ingrese el actor principal: "))
            director = str(input("Ingrese el director: "))
            temporadas = str(input("Ingrese el número de temporadas: "))
            costo_renta = str(input("Ingrese el costo de renta: "))
            costo_venta = str(input("Ingrese el costo de venta: "))
            # se unen los datos sobre la pelicula en un solo renglon
            # es necesario que los datos anteriores sean del tipo string para poder añadirlos al arcivo
            producto = 'Título: ' + titulo + '   Actriz o actor principal: ' + actor_principal + '   Directora o director: ' + director + '   Temporadas: ' + temporadas + '   Costo de renta: ' + costo_renta + '   Costo de venta: ' + costo_venta + '\n'
            Series = open('Series.txt', 'a') # Abrir el archivo Series.txt como escritura para poder agregar al final
            Series.write(producto) # Escribir la información de la serie en el archivo
            Series.close() #se cierra el archivo para actualizarlo
            Existe_tipo = True  # existe una categoria
            print("Serie agregada correctamente.") # mensaje de exito

        elif tipo_producto.lower() == "documental":
            # Solicitar información necesaria de la película
            titulo = input("Ingrese el título del producto: ")
            director = str(input("Ingrese el director: "))
            tema = str(input("Ingrese el tema: "))
            año = str(input("Ingrese el año: "))
            costo_renta = str(input("Ingrese el costo de renta: "))
            costo_venta = str(input("Ingrese el costo de venta: "))
            # se unen los datos sobre la pelicula en un solo renglon
            # es necesario que los datos anteriores sean del tipo string para poder añadirlos al arcivo
            producto = 'Título: ' + titulo + '   Directora o director: ' + director + '   Tema: ' + tema + '   Año: ' + año + '   Costo de renta: ' + costo_renta + '   Costo de venta: ' + costo_venta + '\n'
            Documentales = open('Documentales.txt', 'a') # Abrir el archivo Series.txt como escritura para poder agregar al final
            Documentales.write(producto) # Escribir la información de la serie en el archivo
            Documentales.close() #se cierra el archivo para actualizarlo
            Existe_tipo = True  # existe una categoria
            print("Documental agregado correctamente.") # mensaje de exito

        elif tipo_producto.lower() == "evento deportivo en vivo":
            # Solicitar información necesaria de la película
            titulo = input("Ingrese el título del producto: ")
            deporte = str(input("Ingrese el deporte: "))
            fecha = str(input("Ingrese la fecha: "))
            hora = str(input("Ingrese la hora: "))
            lugar = str(input("Ingrese el lugar: "))
            costo_venta = str(input("Ingrese el costo de venta: "))
            # se unen los datos sobre la pelicula en un solo renglon
            # es necesario que los datos anteriores sean del tipo string para poder añadirlos al arcivo
            producto = 'Título: ' + titulo + '   Deporte: ' + deporte + '   Fecha: ' + fecha + '   Hora: ' + hora + '   Lugar: ' + lugar + '   Costo de venta: ' + costo_venta + '\n'
            Eventos_deportivos = open('Eventos_Deportivos.txt', 'a') # Abrir el archivo Series.txt como escritura para poder agregar al final
            Eventos_deportivos.write(producto) # Escribir la información de la serie en el archivo
            Eventos_deportivos.close()#se cierra el archivo para actualizarlo
            Existe_tipo = True # existe una categoria
            print("Evento deportivo en vivo agregado correctamente.") # mensaje de exito
        else:
            # en caso de no encontrar un tipo, no sehacen cambios en la variable Existe_tipo y se repite
            print("Tipo de producto inválido. Intenta de nuevo")

    print("Catálogo actualizado correctamente.") # mensaje de actualizacion