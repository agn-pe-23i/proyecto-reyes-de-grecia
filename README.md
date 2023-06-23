[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto

## Miembros
-Medrano Cano Axel André 
-Ochoa De La Cruz Bryan Tonatiuh
-Gustavo Angel Morales Vigi
## Diagrama de estructura
![DIAGRAMA DE ESTRUCTURA](https://github.com/agn-pe-23i/proyecto-reyes-de-grecia/assets/125324187/e040896b-ac93-43b4-b02b-36000439aa82)




El diagrama de estructura del programa "Servicio Streaming" consta de un módulo principal, este ejecuta múltiples opciones, dependiendo de la elección del usuario.

Los parámetros de entrada de cada función a excepción de: (MOSTRAR_MENU, cargar_catalogo) son 4 listas, ya que estas son las que se utilizan para poder realizar las acciones en cada función, en el caso de la función “cargar_catalogo” no hay parámetros de entrada, puesto que es este quien genera y regresa las listas que se ocupan en las demás funciones.
La función “agregar_producto” usa la función “agregar_registro”, este recibe el producto como cadena de texto y la lista donde se agregará el producto

La función “mostrar catalogo” usa la función “imprimir_catalogo” que recibe una lista, de la cual imprime el contenido


## Documentación
El programa principal solicita al usuario que elija una opción del menú. Dependiendo de la opción seleccionada, se invoca la función correspondiente para realizar los cambios necesarios.

El código utiliza listas como subcatálogos, donde cada una representa una categoría, como Películas, Series, Documentales y Eventos deportivos en vivo. Esto se hace con el fin de facilitar la manipulación de los productos.

En la función "agregar_producto", se solicita al usuario que ingrese la categoría del producto. Si la categoría existe, se le pide al usuario ingresar los detalles del producto. En caso contrario, se repite el paso anterior. Dependiendo de la información ingresada, puede ser necesario solicitar más datos al usuario. Si la entrada es válida, se permite ingresar todos los detalles del producto, que luego se añaden a la categoría correspondiente mediante la función "agregar_registro".

En la función "buscar_producto", se solicitan palabras clave y se realiza una búsqueda en cada una de las categorías. Se comparan las palabras clave con el contenido de las categorías para encontrar resultados similares. Si se encuentra un producto coincidente, se muestra al usuario junto con la categoría a la que pertenece. En caso contrario, se repite la función.

En la función "eliminar_producto", se solicita al usuario el título del producto que desea eliminar. Se busca en cada categoría hasta encontrar el título correspondiente y se elimina de la categoría. Si el título no se encuentra, se reinicia la función desde el principio.

En la función "mostrar_catalogo", se muestra un menú y se solicita al usuario que elija la categoría que desea ver. Dependiendo de la opción seleccionada, se lee la categoría correspondiente y se muestra al usuario el contenido según su elección, utilizando la función "imprimir_catalogo".

En la función "cargar_catalogo", se solicita al usuario el nombre del archivo que desea cargar. Si el archivo existe, se separa el catálogo en sus diferentes categorías y se muestra el mensaje "Archivo cargado correctamente". En caso contrario, se muestra un mensaje de error y se solicita nuevamente la entrada.

En la función "guardar_catalogo", se pide al usuario el nombre del documento en el que se almacenará el catálogo. Si el archivo existe, se escribe el contenido de cada categoría dentro del archivo y se muestra el mensaje "Archivo guardado correctamente". En caso contrario, se muestra un mensaje de error y se solicita nuevamente la entrada.


## Diseño e implementación
El programa principal utiliza un bucle que se repite hasta que el usuario decide salir. En cada iteración del bucle, se muestra el menú principal y se solicita al usuario que elija una opción. Cada opción del menú está asociada a una función específica.

Estos módulos interactúan con el usuario solicitando información relevante y realizando las operaciones correspondientes en el catálogo. Cada módulo se encarga de realizar una tarea específica, como agregar un producto, buscar un producto, eliminar un producto, mostrar el catálogo, cargar un catálogo o guardar un catálogo.

El programa maneja casos de error cuando se intenta realizar una operación sin haber cargado previamente un catálogo.

El programa maneja la información por medio de listas, cada una contiene una categoría, estas son proporcionadas por la función cargar catálogo; esta, usa palabras clave como separadores, los cuales están presentes en el catálogo en todo momento, ya que estos funcionan como subtítulos para separar categorías dentro del archivo, la función busca estos separadores en el documento y mientras no haya cambios en los separadores guardara cada línea/producto, en su lista correspondiente, cuando se ejecuta un cambio de separador los productos se guardan en la lista siguiente.

Una parte del diseño e implementación del programa se basa en el enfoque top-down. Las funciones "agregar_producto" y "mostrar_catalogo" utilizan funciones auxiliares que facilitan el proceso de agregar un producto y mostrar el contenido de una lista, respectivamente, dependiendo de la opción seleccionada por el usuario

