# BIC01: Tercer Laboratorio

## Primera Parte

Implemente un programa que realize lo siguiente:

1. Complete la implementación de la función `palabra_completada`. Esta función tiene dos parámetros: 
   La cadena de caracteres `palabra_secreta` y la lista de letras `letras_seleccionadas`.
   Esta función retorna `True` si es posible formar `palabra_secreta` con las letras en `letras_seleccionadas`.
   Por ejemplo:
   
    ```python
        palabra_secreta = "apple"
        letras_seleccionadas = ["e", "i", "k", "p", "r", "s"]
        print(palabra_completada(palabra_secreta, letras_seleccionadas))  # Debe mostrar: False
    ```

2. Complete la implementación de la función `obtener_solucion_como_cadena`. Esta función tiene dos parámetros: 
   La cadena de caracteres `palabra_secreta` y la lista de letras `letras_seleccionadas`.
   Esta función transforma el contenido de `palabra_secreta`: para cada letra, si se encuentra dentro de 
   `letras_seleccionadas` se muestra tal cual en la cadena resultante.
   Caso contrario, en la cadena resultante se reemplaza mediante guión bajo + espacio (`_ `). Por ejemplo:
   
    ```python
        palabra_secreta = "apple"
        letras_seleccionadas = ["e", "i", "k", "p", "r", "s"]
        print(obtener_solucion_como_cadena(palabra_secreta, letras_seleccionadas))  # Debe mostrar: _ pp_ e
    ```

3. Complete la implementación de la función `obtener_letras_disponibles`. Esta función tiene un parámetro: 
   la lista de letras `letras_seleccionadas`. Esta función retorna una cadena de caracteres, conteniendo las letras 
   del alfabeto que **no** están dentro de `letras_seleccionadas`.
   Por ejemplo:
   
    ```python
        letras_seleccionadas = ["e", "i", "k", "p", "r", "s"]
        print(obtener_letras_disponibles(letras_seleccionadas))  # Debe mostrar: abcdfghjlmnoqtuvwxyz
    ```

## Segunda Parte

Complete la implementación de la función `iniciar`. Esta función tiene un parámetro: la cadena de caracteres 
`palabra_secreta`, representando la palabra a adivinar en 
un [juego del ahorcado](https://es.wikipedia.org/wiki/Ahorcado_(juego)). En su implementación, haga uso de las funciones 
desarrolladas en la primera parte.

Las reglas del juego son las siguientes:

* Los usuarios empiezan el juego con 6 oportunidades. El programa mostrará al inicio del juego el número de letras de 
`palabra_secreta`.  En cada oportunidad, pueden ingresar la letra que creen pertenece 
a `palabra_secreta`.
  
* Antes de ingresar la letra, el programa mostrará el número de oportunidades disponibles y que letras aún no han sido 
ingresadas por el usuario.
  
* Después de ingresar una letra, el programa mostrará si la letra pertenece o no a `palabra_secreta`. Las letras pendientes 
serán mostradas con guion bajo + espacio (`_ `). Por ejemplo:
  
    ```
    Cargando palabras desde archivo...
       127 palabras en diccionario.
    Este es el juego del ahorcado!
    Adivina el pais. Tiene 4 letras.
    -----------
    Te quedan 6 oportunidades.
    Letras disponibles: abcdefghijklmnopqrstuvwxyz
    Ingresa una letra: a
    Exito!: _ _ _ a
    Te quedan 6 oportunidades.
    Letras disponibles: bcdefghijklmnopqrstuvwxyz
    Ingresa una letra: n
    Error! Esa letra no esta en la palabra: _ _ _ a
    ```

* En cada oportunidad, los usuarios pueden ingresar letras (en mayúsculas o minúsculas) **no ingresadas previamente**. 
  En caso ingresen un carácter 
  inválido, se emitirá una advertencia. Los usuarios al iniciar el juego tienen 3 advertencias disponibles, luego de 
  3 advertencias, un error de carácter inválido les hará perder una oportunidad.

    ```
    Cargando palabras desde archivo...
       127 palabras en diccionario.
    Este es el juego del ahorcado!
    Adivina el pais. Tiene 4 letras.
    -----------
    Te quedan 6 oportunidades.
    Letras disponibles: abcdefghijklmnopqrstuvwxyz
    Ingresa una letra: n
    Error! Esa letra no esta en la palabra: _ _ _ _ 
    Te quedan 5 oportunidades.
    Letras disponibles: abcdefghijklmopqrstuvwxyz
    Ingresa una letra: n
    Error! Ya has ingresado esa letra. Te quedan 2 advertencias: _ _ _ _ 
    Te quedan 5 oportunidades.
    Letras disponibles: abcdefghijklmopqrstuvwxyz
    Ingresa una letra: $
    Error! No es una letra valida. Te quedan 1 advertencias: _ _ _ _ 
    Te quedan 5 oportunidades.
    Letras disponibles: abcdefghijklmopqrstuvwxyz
    ```
  
* En caso la letra ingresada sea una consonante y no pertenezca a `palabra_secreta`, el usuario perderá una oportunidad.
  Si la letra es una vocal, el usuario perderá dos oportunidades.
  
* En caso el usuario se quede sin oportunidades, el juego termina y el usuario ha perdido. Se mostrará en pantalla 
  la `palabra_secreta` que debió adivinarse. Por ejemplo:
  
    ```
    Cargando palabras desde archivo...
       127 palabras en diccionario.
    Este es el juego del ahorcado!
    Adivina el pais. Tiene 4 letras.
    -----------
    Te quedan 6 oportunidades.
    Letras disponibles: abcdefghijklmnopqrstuvwxyz
    Ingresa una letra: p
    Error! Esa letra no esta en la palabra: _ _ _ _ 
    Te quedan 5 oportunidades.
    Letras disponibles: abcdefghijklmnoqrstuvwxyz
    Ingresa una letra: e
    Error! Esa letra no esta en la palabra: _ _ _ _ 
    Te quedan 3 oportunidades.
    Letras disponibles: abcdfghijklmnoqrstuvwxyz
    Ingresa una letra: r
    Error! Esa letra no esta en la palabra: _ _ _ _ 
    Te quedan 2 oportunidades.
    Letras disponibles: abcdfghijklmnoqstuvwxyz
    Ingresa una letra: u
    Exito!: _ u_ _ 
    Te quedan 2 oportunidades.
    Letras disponibles: abcdfghijklmnoqstvwxyz
    Ingresa una letra: o
    Error! Esa letra no esta en la palabra: _ u_ _ 
    Te quedan 0 oportunidades.
    Letras disponibles: abcdfghijklmnqstvwxyz
    Ingresa una letra: h
    Error! Esa letra no esta en la palabra: _ u_ _ 
    Lo siento, te quedaste sin oportunidades. El pais era cuba
    ```
  
* En caso el usuario adivine la palabra, el juego termina y el usuario ha ganado. Se mostrará en pantalla un mensaje 
  con su puntaje. El puntaje es el producto de el numero de oportunidades disponibles y el numero de letras unicas en
  `palabra_secreta`. Por ejemplo:

    ```
    Cargando palabras desde archivo...
       127 palabras en diccionario.
    Este es el juego del ahorcado!
    Adivina el pais. Tiene 4 letras.
    -----------
    Te quedan 6 oportunidades.
    Letras disponibles: abcdefghijklmnopqrstuvwxyz
    Ingresa una letra: c
    Exito!: c_ _ _ 
    Te quedan 6 oportunidades.
    Letras disponibles: abdefghijklmnopqrstuvwxyz
    Ingresa una letra: u
    Exito!: cu_ _ 
    Te quedan 6 oportunidades.
    Letras disponibles: abdefghijklmnopqrstvwxyz
    Ingresa una letra: b
    Exito!: cub_ 
    Te quedan 6 oportunidades.
    Letras disponibles: adefghijklmnopqrstvwxyz
    Ingresa una letra: a
    Exito!: cuba
    Felicitaciones, ganaste!
    El puntaje obtenido es 24
    ```

## Tercera Parte

Desarrolle una versión alternativa del juego del ahorcado, donde el usuario pueda solicitar y recibir
ayuda.
Para esto, realice lo siguiente:

1. Complete la implementación de la función `es_solucion_candidata`. Esta función tiene dos parámetros:
   `solucion_como_cadena` es una cadena de caracteres, representando una solución incompleta al juego del 
   ahorcado (incluyendo guiones bajos y espacios). `candidato` es una palabra representada con una cadena de caracteres.
   Esta función retorna `True` si la palabra `candidato`  **puede** ser la solución de `solucion_como_cadena` dentro 
   del juego del ahorcado. Por ejemplo:
   
   ```python
    print(es_solucion_candidata("pi_ u", "peru"))  # Debe mostrar: False
    print(es_solucion_candidata("p_ _ u", "peru"))  # Debe mostrar: True
    print(es_solucion_candidata("canad_ ", "canada"))  # Debe mostrar: False. La letra "a" ya ha sido revelada, por lo que 
                                                       # la ultima letra en "canad_ " NO puede ser "a"
   ```

2. Complete la implementación de la función `mostrar_candidatos`. Esta función tiene un parámetro: 
   `solucion_como_cadena` es una cadena de caracteres, representando una solución incompleta al juego del 
   ahorcado (incluyendo guiones bajos y espacios). Esta función muestra en consola las palabras en la lista 
   `diccionario` que **pueden** ser la solución de `solucion_como_cadena` dentro 
   del juego del ahorcado. `diccionario` es una lista de cadenas de caracteres ubicada en el ámbito global.
   Por ejemplo:
   
    ```python
    mostrar_candidatos("c _ _ _")  # Debe mostrar: chad cuba
    ```
3. Complete la implementación de la función `iniciar_con_ayuda`. Esta función tiene un parámetro: la cadena de caracteres 
    `palabra_secreta`, representando la palabra a adivinar en 
    un [juego del ahorcado](https://es.wikipedia.org/wiki/Ahorcado_(juego)). En su implementación, haga uso de las funciones 
    desarrolladas previamente. En esta versión, cuando el usuario ingresa el carácter asterisco (`*`) el programa muestra 
   una lista de palabras que podrian ser la solución. El uso de `*` no disminuye el numero de oportunidades o advertencias.
   Por ejemplo:
   
    ```
    Cargando palabras desde archivo...
       127 palabras en diccionario.
    Este es el juego del ahorcado!
    Adivina el pais. Tiene 4 letras.
    -----------
    Te quedan 6 oportunidades.
    Letras disponibles: abcdefghijklmnopqrstuvwxyz
    Ingresa una letra: c
    Exito!: c_ _ _ 
    Te quedan 6 oportunidades.
    Letras disponibles: abdefghijklmnopqrstuvwxyz
    Ingresa una letra: h
    Error! Esa letra no esta en la palabra: c_ _ _ 
    Te quedan 5 oportunidades.
    Letras disponibles: abdefgijklmnopqrstuvwxyz
    Ingresa una letra: *
    Posibles candidatos:
    chad cuba
    Te quedan 5 oportunidades.
    Letras disponibles: abdefgijklmnopqrstuvwxyz
    Ingresa una letra: a
    Exito!: c_ _ a
    Te quedan 5 oportunidades.
    Letras disponibles: bdefgijklmnopqrstuvwxyz
    Ingresa una letra: u
    Exito!: cu_ a
    Te quedan 5 oportunidades.
    Letras disponibles: bdefgijklmnopqrstvwxyz
    Ingresa una letra: b
    Exito!: cuba
    Felicitaciones, ganaste!
    El puntaje obtenido es 20
    ```
   
La implementación debe realizarse en el archivo `ahorcado.py`, entre las líneas marcadas como `#INICIO` y `#FIN`. 
**No remueva o modifique el código base**.

Los mensajes en consola **deben** de los ejemplos contenidos en esta página.