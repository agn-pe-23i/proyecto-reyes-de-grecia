
def guardar_catalogo():
    # Lista de nombres de archivos a fusionar
    nombres_archivos = ['Peliculas.txt', 'Series.txt', 'Documentales.txt', 'Eventos_deportivos.txt']

    # Abrir 'catalogo.txt' en modo de escritura ('w')
    # para borrar cualquier contenido previo en el archivo se escribe una cadena vacia
    with open('catalogo.txt', 'w') as archivo_catalogo:
        archivo_catalogo.write("")

    # Abrir 'catalogo.txt' en modo de anexado ('a')
    # para agregar el contenido de los archivos a fusionar
    with open('catalogo.txt', 'a') as catalogo:
        # Iterar sobre los nombres de los archivos
        for archivo in nombres_archivos:
            # Abrir cada archivo en modo de lectura ('r') para agregarlo al catalogo principal
            with open(archivo, 'r') as contenido:
                catalogo.write(contenido.read()) # Escribir el contenido del archivo en 'catalogo.txt'

    print("Catálogo actualizado correctamente.") # Mostrar mensaje de éxito