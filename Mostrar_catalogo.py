
def mostrar_catalogo():
    Salir = False #variable para salir
    while not Salir:
        print("\n-- Menú mostrar catálogo --") #imprime el menu
        print("1. Películas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos deportivos")
        print("5. Todo")
        print("6. Regresar")

        opcion = input("Seleccione una opción: ")

        # Leer el contenido del archivo Peliculas.txt y asignarlo a la variable Peliculas
        Categoria = open('Peliculas.txt', 'r')
        Peliculas = Categoria.read()
        Categoria.close()
        # Leer el contenido del archivo Series.txt y asignarlo a la variable Series
        Categoria_2 = open('Series.txt', 'r')
        Series = Categoria_2.read()
        Categoria.close()
        # Leer el contenido del archivo documentales.txt y asignarlo a la variable Documentales
        Categoria_3 = open('Documentales.txt', 'r')
        Documentales = Categoria_3.read()
        Categoria.close()
        # Leer el contenido del archivo Eventos_Deportivos.txt y asignarlo a la variable Eventos_deportivos
        Categoria_4 = open('Eventos_Deportivos.txt', 'r')
        Eventos_Deportivos = Categoria_4.read()
        Categoria.close()

        if opcion == "1":
            print('\n', Peliculas)  #mostrar el contenido en Peliculas

        elif opcion == "2":
            print('\n', Series) #mostrar el contenido en Series

        elif opcion == "3":
            print('\n', Documentales) #mostrar el contenido en Documentales

        elif opcion == "4":
            print('\n', Eventos_Deportivos) #mostrar el contenido en Eventos_Deportivos

        elif opcion == "5":
            # mostrar el contenido completo
            print('\n', Peliculas, '\n', Series, '\n', Documentales, '\n', Eventos_Deportivos)
        elif opcion == "6":
            Salir = True #variable salida es verdadera para salir
        else:
            print("Opción inválida.\n Intenta de nuevo")