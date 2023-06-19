
def buscar_producto():
    Existe_producto = False #variable para indicar si existe el producto
    while not Existe_producto:
        clave_busqueda = str(input("Ingrese las palabras clave del título del producto: "))
        archivo = open('Catalogo.txt', 'r') # Abrir el archivo Catalogo.txt en modo de lectura
        for linea in archivo: # se busca en cada linea del catalogo
            # si la clave se encuentra en el catalogo se imprime la línea que contiene la clave de búsqueda
            if clave_busqueda.lower() in linea.lower():
                print(f"'{linea}'")
                Existe_producto = True # la variable es vardadera para dar salida a la busqueda
        archivo.close()
        if not Existe_producto: # en caso de no encontrarse el producto, se continua la busqueda con una cave nueva
            print('El producto no existe, intenta de nuevo')