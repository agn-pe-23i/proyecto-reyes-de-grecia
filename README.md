[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto

## Miembros
-Medrano Cano Axel André 
-Ochoa De La Cruz Bryan Tonatiuh
-Gustavo Angel Morales Vigi
## Diagrama de estructura


El diagrama de estructura del programa "Servicio Streaming" consta de dos módulos principales. El primero se encarga de mostrar el menú de opciones al usuario. El segundo módulo se encarga de ejecutar una instrucción específica en función de la opción seleccionada por el usuario.

Dentro del segundo módulo, se encuentran seis submódulos que están nombrados de acuerdo a la acción que realizan. Estos submódulos permiten realizar operaciones como solicitar, borrar, agregar y actualizar los productos en la plataforma.

## Documentación
El programa principal solicita al usuario que elija una opción del menú. Dependiendo de la opción seleccionada, se invoca el módulo correspondiente para realizar los cambios necesarios.

En el módulo "agregar_producto", se verifica si existe una categoría y se solicita al usuario ingresar los detalles del producto. Dependiendo de la información ingresada, puede ser necesario solicitar más datos o, si la entrada es válida, se permite al usuario ingresar todos los detalles del producto, que luego se añaden al catálogo.

En el módulo "buscar_producto", se solicitan palabras clave y se realiza una búsqueda en el catálogo en minúsculas para encontrar resultados similares que coincidan con las palabras clave proporcionadas.

En el módulo "eliminar_producto", se solicita al usuario el título del producto a eliminar. Se busca en cada tipo de producto hasta encontrar el título correspondiente y eliminarlo del catálogo.

En el módulo "mostrar_catalogo", se muestra un menú y se solicita al usuario que elija qué desea ver. Dependiendo de la opción seleccionada, se lee el catálogo correspondiente y se muestra al usuario de acuerdo con su elección.

En el módulo "cargar_catalogo", se solicita al usuario el nombre del archivo que desea ver. Si el archivo existe, se muestra el contenido. En caso contrario, se muestra un mensaje de error y se solicita nuevamente la entrada.

En el módulo "guardar_catalogo", se actualiza el catálogo original fusionándose con otros catálogos individuales.


## Diseño e implementación
El programa principal realiza un bucle que se repite hasta que el usuario decide salir. En cada iteración del bucle, se muestra el menú principal y se solicita al usuario que elija una opción.
El programa interactúa con el usuario mostrando mensajes de texto para solicitar entradas y proporcionar retroalimentación. Además, se manejan casos de error cuando se intenta realizar una operación sin haber cargado un catálogo previamente.
Algo a destacar es que el programa hace una copia del catálogo original, este no se ve afectado hasta que el usuario elige la opción de guardar catalogo, esto lo hace con el uso de cuatro catálogos, cada uno guarda productos de una categoría en específico, y cuando se ejecuta el guardado, el contenido de estos son reescritos en el catálogo original.

La implementación del programa se basa en el diseño top down, cada opción del menú está asociada a un módulo en específico.
Estos módulos interactúan con el usuario solicitando información relevante y realizando las operaciones correspondientes en el catálogo.
Cada módulo se encarga de realizar una tarea determinada, como agregar un producto, buscar un producto, eliminar un producto, mostrar el catálogo, cargar un catálogo o guardar un catálogo (dependiendo de cada opción es si pasamos de solamente leer e imprimir un archivo a editarlo).
