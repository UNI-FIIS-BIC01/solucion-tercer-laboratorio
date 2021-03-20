import random
import string

ARCHIVO_DICCIONARIO = "diccionario.txt"


def cargar_diccionario():
    print("Cargando palabras desde archivo...")

    with open(ARCHIVO_DICCIONARIO, 'r') as archivo_diccionario:
        lineas = archivo_diccionario.readlines()

    lista_palabras = [linea.strip().lower() for linea in lineas]
    print("  ", len(lista_palabras), "palabras en diccionario.")
    return lista_palabras


def seleccionar_palabra(lista_palabras):
    return random.choice(lista_palabras)


# IMPORTANTE! No modificar el codigo encima de esta linea.

diccionario = cargar_diccionario()


def palabra_completada(palabra_secreta, letras_seleccionadas):
    """

    :param palabra_secreta: Cadena de caracteres.
    :param letras_seleccionadas: Lista. Contiene letras como cadenas de caracteres.
    :return: True si se ha completado la palabra con las letras en letras_correctas.
    Falso en caso contrario.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO

    for letra in palabra_secreta:
        if letra not in letras_seleccionadas:
            return False

    return True
    # FIN


def obtener_solucion_como_cadena(palabra_secreta, letras_seleccionadas):
    """

    :param palabra_secreta: Cadena de caracteres.
    :param letras_seleccionadas: Lista. Contiene letras como cadenas de caracteres.
    :return: Una cadena de caracteres conteniendo letras y guiones bajos (_), en base a si
    las letras en letras_seleccionadas pertenecen a palabra_secreta.
    Las letras pendientes se representan mediante guion bajo + espacio en blanco.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    solucion_como_cadena = ""

    for letra in palabra_secreta:
        if letra in letras_seleccionadas:
            solucion_como_cadena += letra
        else:
            solucion_como_cadena += "_ "

    return solucion_como_cadena
    # FIN


def obtener_letras_disponibles(letras_seleccionadas):
    """

    :param letras_seleccionadas: Lista. Contiene letras como cadenas de caracteres.
    :return: Una cadena de caracteres. Contiene las letras del alfabeto NO incluidas en letras_seleccionadas.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    letras_disponibles = ""
    for letra in string.ascii_lowercase:
        if letra not in letras_seleccionadas:
            letras_disponibles += letra

    return letras_disponibles
    # FIN


def error_con_advertencia(oportunidades, advertencias, razon, solucion_como_cadena):
    if advertencias >= 1:
        advertencias -= 1
    else:
        oportunidades -= 1

    print("Error! " + razon + ". Te quedan " + str(advertencias) + " advertencias: " +
          solucion_como_cadena)

    return oportunidades, advertencias


def mostrar_ganador(oportunidades, palabra_secreta):
    print("Felicitaciones, ganaste!")

    letras_unicas = []
    for letra in palabra_secreta:
        if letra not in letras_unicas:
            letras_unicas.append(letra)

    puntaje = oportunidades * len(letras_unicas)
    print("El puntaje obtenido es " + str(puntaje))


def error_letra_incorrecta(penalidad, oportunidades, solucion_como_cadena):
    oportunidades -= penalidad
    print("Error! Esa letra no esta en la palabra: " + solucion_como_cadena)
    return oportunidades


def iniciar_ahorcado(palabra_secreta, con_ayuda):
    print("Este es el juego del ahorcado!")
    print("Adivina el pais. Tiene " + str(len(palabra_secreta)) + " letras.")
    print("-----------")

    letras_seleccionadas = []
    oportunidades = 6
    advertencias = 3

    while not palabra_completada(palabra_secreta, letras_seleccionadas) and oportunidades >= 0:
        print("Te quedan " + str(oportunidades) + " oportunidades.")
        print("Letras disponibles: " + obtener_letras_disponibles(letras_seleccionadas))

        letra = input("Ingresa una letra: ").lower()

        if con_ayuda and letra == "*":
            print("Posibles candidatos:")
            mostrar_candidatos(obtener_solucion_como_cadena(palabra_secreta,
                                                            letras_seleccionadas))
        elif not letra.isalpha():
            oportunidades, advertencias = error_con_advertencia(oportunidades, advertencias, "No es una letra valida",
                                                                obtener_solucion_como_cadena(palabra_secreta,
                                                                                             letras_seleccionadas))
        elif letra in letras_seleccionadas:
            oportunidades, advertencias = error_con_advertencia(oportunidades, advertencias,
                                                                "Ya has ingresado esa letra",
                                                                obtener_solucion_como_cadena(palabra_secreta,
                                                                                             letras_seleccionadas))
        elif letra in palabra_secreta:
            letras_seleccionadas.append(letra)
            print("Exito!: " + obtener_solucion_como_cadena(palabra_secreta, letras_seleccionadas))

        elif letra not in palabra_secreta and letra in "aeiou":
            letras_seleccionadas.append(letra)
            oportunidades = error_letra_incorrecta(2, oportunidades, obtener_solucion_como_cadena(palabra_secreta,
                                                                                                  letras_seleccionadas))

        elif letra not in palabra_secreta and letra not in "aeiou":
            letras_seleccionadas.append(letra)
            oportunidades = error_letra_incorrecta(1, oportunidades, obtener_solucion_como_cadena(palabra_secreta,
                                                                                                  letras_seleccionadas))
    if palabra_completada(palabra_secreta, letras_seleccionadas):
        mostrar_ganador(oportunidades, palabra_secreta)
    else:
        print("Lo siento, te quedaste sin oportunidades. El pais era " + palabra_secreta)


def iniciar(palabra_secreta):
    """
    Reglas del juego:
    - Los jugadores pueden ingresar letras, mayusculas o minusculas.
    - Cada juego inicia con 6 oportunidades y 3 advertencias.
    - Los jugadores pierden una advertencia al ingresar letras repetidas o caracteres invalidos.
    - Cuando las advertencias se agotan, las letras repetidas o caracteres invalidos reducen el numero de oportunidades
    en uno.
    - Cuando los jugadores ingresan una letra que SI esta en palabra_secreta, no pierden oportunidades.
    - Cuando los jugadores ingresan una vocal que NO esta en palabra_secreta, pierden 2 oportunidades.
    - Cuando los jugadores ingresan una consonante que NO esta en palabra_secreta, pierden 1 oportunidad.
    - Cuando un jugador se ha quedado sin oportunidades, pierde el juego.
    - Cuando un jugador adivina la palabra, gana el juego. Su puntaje es el numero de oportunidades restantes * el numero de
    letras unicas en palabra_secreta.

    :param palabra_secreta: Palabra a adivinar.
    :return: None.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    iniciar_ahorcado(palabra_secreta, False)
    # FIN


def es_solucion_candidata(solucion_como_cadena, candidato):
    """

    :param solucion_como_cadena: Cadena de caracteres. Contiene una solucion parcial, incluyendo guiones bajos _
    y espacios en blanco.
    :param candidato: Una potencial solucion para solucion_como_cadena
    :return: True, si candidato podria ser una solucion valida para solucion_como_cadena. Falso caso contrario.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO

    solucion_como_cadena = solucion_como_cadena.replace(" ", "")

    if len(solucion_como_cadena) != len(candidato):
        return False

    caracteres_revelados = []
    for letra in solucion_como_cadena:
        if letra != "_":
            caracteres_revelados.append(letra)

    for indice in range(len(solucion_como_cadena)):
        caracter_solucion = solucion_como_cadena[indice]
        caracter_candidato = candidato[indice]

        if caracter_solucion != "_" and caracter_solucion != caracter_candidato:
            return False

        if caracter_solucion == "_" and caracter_candidato in caracteres_revelados:
            return False

    return True

    # FIN


def mostrar_candidatos(solucion_como_cadena):
    """

    Muestra en consola las palabras contenidas en diccionario (variable global) que pueden ser soluciones validas a
    solucion_como_cadena.

    :param solucion_como_cadena: Cadena de caracteres. Contiene una solucion parcial, incluyendo guiones bajos _
    y espacios en blanco.
    :return: None.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO

    candidatos = []
    for pais in diccionario:
        if es_solucion_candidata(solucion_como_cadena, pais.lower()):
            candidatos.append(pais)

    print(" ".join(candidatos))

    # FIN


def iniciar_con_ayuda(palabra_secreta):
    """

    Las reglas son las mismas que el juego de ahorcado normal. Sin embargo, cuando el usuario ingresa *, se muestra un
    listado de potenciales soluciones de acuerdo a las letras que a adivinado a la fecha. El usar * no disminuye el
    numero de oportunidades o advertencias.

    :param palabra_secreta: Palabra a adivinar.
    :return: None.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    iniciar_ahorcado(palabra_secreta, True)
    # FIN
    return


if __name__ == "__main__":
    palabra_secreta = seleccionar_palabra(diccionario)
    iniciar_con_ayuda(palabra_secreta)

