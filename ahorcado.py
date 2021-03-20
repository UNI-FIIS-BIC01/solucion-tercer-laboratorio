import random

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

    # FIN
    return


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

    # FIN
    return


def obtener_letras_disponibles(letras_seleccionadas):
    """

    :param letras_seleccionadas: Lista. Contiene letras como cadenas de caracteres.
    :return: Una cadena de caracteres. Contiene las letras del alfabeto NO incluidas en letras_seleccionadas.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO

    # FIN
    return


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

    # FIN
    return


def es_solucion_candidata(solucion_como_cadena, candidato):
    """

    :param solucion_como_cadena: Cadena de caracteres. Contiene una solucion parcial, incluyendo guiones bajos _
    y espacios en blanco.
    :param candidato: Una potencial solucion para solucion_como_cadena
    :return: True, si candidato podria ser una solucion valida para solucion_como_cadena. Falso caso contrario.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO

    # FIN
    return


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

    # FIN
    return


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

    # FIN
    return


if __name__ == "__main__":
    palabra_secreta = seleccionar_palabra(diccionario)
    iniciar(palabra_secreta)

    # Para iniciar ahorcado con ayuda, ejecutar
    # iniciar_con_ayuda(palabra_secreta)
