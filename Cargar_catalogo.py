
def cargar_catalogo():
    """
    Solicita el nombre del archivo que se va a cargar

    En caso de no poder abrirlo, vuelve a pedir el nombre

    Separa las categorias en listas, apoyando de de separadores que indican el
    cambio de categoria dento del texto del documento

    Regresa las listas de cada categoria y la variable Hay_catalogo
    """

    archivo_encontrado = False #Mientras archivo_encontrado es falso se repite el bucle para pedir el nombre
    catalogo = [] #se crea el catalogo como lista para almecenar las listas de las categorias
    Hay_catalogo = False #Hay_catalogo es falso hasta que se carge el catalogo

    nombre_archivo = input("Ingrese el nombre del archivo del catálogo: ")  # Recibe el nombre del archivo que contiene el catalogo
    while not archivo_encontrado:
        try: #intenta abrir el archivo y si es posible se ejecuta:
            with open(nombre_archivo, "r") as archivo: #se abre el archivo en modo lectura
                catalogo = archivo.read() #Se guarda el contenido del catalogo
            archivo_encontrado = True #variable verdadera para dar salida al bucle
            Hay_catalogo = True #Variable verdadera, se cargo el catalogo

        except FileNotFoundError: # si el intento fallo se ejecuta:
            print("El archivo no existe.") #si no se encuentra el archivo, se manda mensaje de error y se invita a intentar de nuevo
            print("Ingrese el nombre del archivo del catálogo nuevamente: ") # Recibe el nombre del archivo que contiene el catalogo

    """
    los separdores se usaran para saber en que momento camia de categoria (En el catalogo hay subtitulos que indican la categoria)
    Se usan estos subtitulos para compararlos con cada linea del catalogo y mientras no haya cambio se guarda cada linea
     
    """
    separadores = ['Series:', 'Documentales:', 'Eventos deportivos en vivo:'] #Se declaran los separadores de apoyo

    #Se crean las listas para cada categoria
    lista_peliculas = []
    lista_series = []
    lista_documentales = []
    lista_eventos_en_vivo = []

    numero_lista = 0 # se declara el numero de lista como 0

    for linea in catalogo.split('\n'): #Se evalua cada lnea del catalogo
                                    #mientras no haya cambio en el separador se agrega cada linea a su lista correspondiente
        if linea in separadores:
            numero_lista += 1
        if numero_lista == 0:
            lista_peliculas.append(linea)
        elif numero_lista == 1:
            lista_series.append(linea)
        elif numero_lista == 2:
            lista_documentales.append(linea)
        elif numero_lista == 3:
            lista_eventos_en_vivo.append(linea)


    print("Archivo cargado correctamente.") #mensaje de exito
    return Hay_catalogo, lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo #Regresa la variable Hay_catalogo y las listas de cada categoria