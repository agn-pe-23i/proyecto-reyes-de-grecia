def imprimir_catalogo(lista):
    for elemento in lista:
        print(elemento)

def mostrar_catalogo(lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo):
    """
        se reciben  las listas de cada categoria para poder mostrar su contenido:
        lista_peliculas
        lista_series
        lista_documentales
        lista_eventos_en_vivo

        Muestra el menú del catalogo con las distintas categorias
        Solicita una opcion al usuario
        Imprime el contenido del catalogo por categoria e incluso el catalogo completo

        """
    Salir = False #Mientras Salir es falso se repite el bucle
    while not Salir:
        print("\n-- Menú mostrar catálogo --") #imprime el menu
        print("1. Películas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos deportivos")
        print("5. Todo")
        print("6. Regresar")

        opcion = input("Seleccione una opción: ") #Recibe opcion del usuario


        if opcion == "1":
            imprimir_catalogo(lista_peliculas)  #mostrar el contenido en Peliculas

        elif opcion == "2":
            imprimir_catalogo(lista_series) #mostrar el contenido en Series

        elif opcion == "3":
            imprimir_catalogo(lista_documentales) #mostrar el contenido en Documentales

        elif opcion == "4":
            imprimir_catalogo(lista_eventos_en_vivo) #mostrar el contenido en Eventos_Deportivos

        elif opcion == "5":
            # mostrar el contenido completo
            listas = lista_peliculas, lista_series, lista_documentales, lista_eventos_en_vivo #Se agrupan las listas para darles porcicion
            for lista in listas:
                imprimir_catalogo(lista)    #Se imprimen todas las listas de la lista listas
        elif opcion == "6":
            Salir = True #variable salida es verdadera para salir
        else:
            print("Opción inválida.\n Intenta de nuevo") # si la opcion no se encuentra, se manda mensaje de error y se invita a intentar de nuevo
