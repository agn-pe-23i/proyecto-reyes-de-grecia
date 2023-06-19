
def cargar_catalogo():
    # Solicitar al usuario el nombre del archivo del catalogo
    nombre_archivo = input("Ingrese el nombre del archivo del catalogo: ")
    archivo_encontrado = False # Variable que indica si se encontró el archivo
    catalogo = [] # Lista para almacenar el contenido del catálogo

    while not archivo_encontrado:
        try: # Intentar abrir el archivo en modo de lectura ('r')
            with open(nombre_archivo, "r") as archivo: #Abrir el archivo y asignarlo en archivo
                catalogo = archivo.read() # Leer el contenido del archivo y asignarlo en catalogo
            archivo_encontrado = True # El archivo se ha encontrado
            print("Archivo cargado correctamente.") # Mensaje de exito
        except FileNotFoundError: #Si no se encontro el archivo
            print("El archivo no existe.") #Mensaje de Fracaso
            nombre_archivo = input("Ingrese el nombre del archivo del catalogo nuevamente: ")

    return catalogo