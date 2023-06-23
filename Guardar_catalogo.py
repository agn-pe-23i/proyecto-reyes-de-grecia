def guardar_catalogo(lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo):
    """
        se reciben  las listas de cada categoria para hacer la actualizacion del catalogo:
        lista_peliculas
        lista_series
        lista_documentales
        lista_eventos_en_vivo

        Solicita el nombre del archivo donde se guardara el catalogo
        En caso de no poder abrirlo, vuelve a pedir el nombre

        Borra el contenido del catalogo
        Escribe en el catalogo las listas de categiorias




        """
    # Lista de nombres de archivos a fusionar
    listas = lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo

    # Solicitar al usuario el nombre del archivo del catalogo
    nombre_archivo = input("Ingrese el nombre del archivo donde se guardara el catalogo: ")
    archivo_encontrado = False  # Variable que indica si se encontró el archivo

    while not archivo_encontrado:
        try:  # Intentar abrir el archivo en modo de escritura
            with open(nombre_archivo, "w") as archivo:  # Abrir el archivo y asignarlo en archivo
                catalogo = archivo.write('')  # Leer el contenido del archivo y asignarlo en catalogo
            with open(nombre_archivo, 'a') as archivo:
                for lista in listas:
                    for elemento in lista:
                        catalogo= archivo.write(elemento + '\n')
            archivo_encontrado = True  # El archivo se ha encontrado
            print("Catálogo actualizado correctamente.")  # Mostrar mensaje de éxito

        except FileNotFoundError:  # Si no se encontro el archivo
            print("El archivo no existe.")  # Mensaje de Fracaso
            nombre_archivo = input("Ingrese el nombre del archivo del catalogo nuevamente: ")
