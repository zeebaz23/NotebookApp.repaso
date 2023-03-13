# Libreta de notas (Notebook)
Esta es una aplicación de práctica de conceptos de programación 
orientada a objetos en python, en la cual se quiere implementar 
una libreta de notas. El modelo del mundo del problema para dicha 
aplicación es el siguiente:

![Modelo del mundo del problema aplicación Notebook](assets/images/class-model.png "Modelo del mundo")

El código de la aplicación se encuentra incompleto. La idea es completarlo teniendo en cuenta
los siguientes pasos:

1. En el módulo notebook.py cree una clase `Note` que tenga los siguientes constantes: `HIGH (str)`,
`MEDIUM (str)` y `LOW (str)` y asígnele valores string iguales a sus nombres.
2. En la clase `Note`, agregue los siguientes atributos: `code (int)`, `title (str)`, `text (str)`, 
`creation_date (datetime)`, `importance (str)` y `tags (list[str])`. En el método inicializador reciba los
parámetros `code`, `title`, `text` e `importance` para inicializar los atributos correspondientes. El atributo
`creation_date` inicialícelo usando la expresión `datetime.now()` y el atributo `tags` inicialícelo como
una lista vacía.
3. En la clase `Note`, defina un método de instancia `add_tag` que recibe como parámetro un string `tag`.
En el método debe verificar si el `tag` no se encuentra en la lista `tags`, entonces lo debe agregar.
4. En la clase `Note`, defina un método especial `__str__` que retorna un string. Este método debe retornar un
string que contenga el código de la nota (`code`), un salto de línea (`\n`), la fecha de creación de la nota 
(`creation_date`) de la nota, otro salto de línea (`\n`), el título (`title`) y el texto (`text`) de la siguiente forma:

    ```
    Código: code
    Fecha: creation_date
    title: text
    ```

5. En el módulo notebook.py, cree una clase `Notebook` la cual tiene un atributo `notes` que es un diccionario
donde la clave son enteros (`int`) y los valores son objetos de la clase `Note`. En el método inicializador,
inicialice el atributo `notes` como un diccionario vacío.
6. En la clase `Notebook`, defina un método de instancia `add_note` que recibe los parámetros `title (str)`,
`text (str) `e `importance (str)` y retorna un valor de tipo `int`. En el cuerpo del método implemente el código
necesario para hacer lo siguiente:
   - Generar un `code` que sea igual al número de elementos en el diccionario `notes` más uno.
   - Crear un objeto de la clase `Note`.
   - Agregar el objeto de la clase `Note` al diccionario, utilizando como clave el `code` generado.
   - Retornar el `code`.
7. En la clase `Notebook`, defina un método de instancia `important_notes` que retorne una lista de objetos de la 
clase `Note`. En el cuerpo del método, utilice un _list comprehension_ para crear una lista con todos los objetos
del diccionario `notes` que tienen el atributo `importance` igual a `HIGH` o `MEDIUM`.
8. En la clase `Notebook`, defina un método de instancia `tags_note_count` el cual retorna un diccionario donde las
claves son de tipo `str` y los valores de tipo `int`. En el cuerpo del método implemente un algoritmo para construir un
diccionario que indique, por cada tag, cuántos objetos `Note` tienen dicho tag asignado.

**Nota: Debe utilizar pistas de tipos en todos los casos donde sea posible**