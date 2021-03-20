import io
import sys
from unittest import TestCase, mock

import ahorcado
from ahorcado import palabra_completada, obtener_solucion_como_cadena, obtener_letras_disponibles


class AhorcadoTest(TestCase):

    def test_palabra_no_completada(self):
        palabra_secreta = "apple"
        letras_seleccionadas = ["e", "i", "k", "p", "r", "s"]

        self.assertEqual(False, palabra_completada(palabra_secreta, letras_seleccionadas))

    def test_palabra_completada(self):
        palabra_secreta = "peru"
        letras_seleccionadas = ["e", "i", "k", "p", "r", "u"]

        self.assertEqual(True, palabra_completada(palabra_secreta, letras_seleccionadas))

    def test_solucion_como_cadena(self):
        palabra_secreta = "apple"
        letras_seleccionadas = ["e", "i", "k", "p", "r", "s"]
        solucion_como_cadena = "_ pp_ e"

        self.assertEqual(solucion_como_cadena, obtener_solucion_como_cadena(palabra_secreta, letras_seleccionadas))

    def test_obtener_letras_disponibles(self):
        letras_seleccionadas = ["e", "i", "k", "p", "r", "s"]
        letras_disponibles = "abcdfghjlmnoqtuvwxyz"

        self.assertEqual(letras_disponibles, obtener_letras_disponibles(letras_seleccionadas))

    @mock.patch('ahorcado.input', create=True)
    def test_ahorcado_exito(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["p", "e", "r", "u"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        ahorcado.iniciar("peru")

        with open("ahorcado_exito.txt", "r") as archivo_salida:
            resultado_esperado = archivo_salida.readlines()

        resultad_actual = resultado_test.getvalue().strip().split('\n')
        self.assertEqual(len(resultado_esperado), len(resultad_actual))

        for linea_esperada, linea_actual in zip(resultado_esperado, resultad_actual):
            self.assertEqual(linea_esperada.strip(), linea_actual.strip())

    @mock.patch('ahorcado.input', create=True)
    def test_ahorcado_error(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["q", "i", "s", "t", "v", "w"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        ahorcado.iniciar("peru")

        with open("ahorcado_error.txt", "r") as archivo_salida:
            resultado_esperado = archivo_salida.readlines()

        resultad_actual = resultado_test.getvalue().strip().split('\n')
        self.assertEqual(len(resultado_esperado), len(resultad_actual))

        for linea_esperada, linea_actual in zip(resultado_esperado, resultad_actual):
            self.assertEqual(linea_esperada.strip(), linea_actual.strip())

    @mock.patch('ahorcado.input', create=True)
    def test_ahorcado_advertencias(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["p", "e", "r", "1", "p", "e", "r", "u"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        ahorcado.iniciar("peru")

        with open("ahorcado_advertencias.txt", "r") as archivo_salida:
            resultado_esperado = archivo_salida.readlines()

        resultad_actual = resultado_test.getvalue().strip().split('\n')
        self.assertEqual(len(resultado_esperado), len(resultad_actual))

        for linea_esperada, linea_actual in zip(resultado_esperado, resultad_actual):
            self.assertEqual(linea_esperada.strip(), linea_actual.strip())

    def test_no_es_solucion_candidata(self):
        solucion_como_cadena = "te_ t"
        solucion_candidata = "tact"

        self.assertEqual(False, ahorcado.es_solucion_candidata(solucion_como_cadena, solucion_candidata))

        solucion_como_cadena = "a_ ple"
        solucion_candidata = "apple"
        self.assertEqual(False, ahorcado.es_solucion_candidata(solucion_como_cadena, solucion_candidata))

    def test_es_solucion_candidata(self):
        solucion_como_cadena = "a_ _ le"
        solucion_candidata = "apple"

        self.assertEqual(True, ahorcado.es_solucion_candidata(solucion_como_cadena, solucion_candidata))

    def test_mostrar_candidatos(self):

        solucion_como_cadena = "chi _ _"

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        ahorcado.mostrar_candidatos(solucion_como_cadena)

        resultado_esperado = "chile china"
        self.assertEqual(resultado_test.getvalue().strip(), resultado_esperado)

    @mock.patch('ahorcado.input', create=True)
    def test_ahorcado_ayuda(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["*", "c", "*", "u", "*", "b", "a"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        ahorcado.iniciar_con_ayuda("cuba")

        with open("ahorcado_ayuda.txt", "r") as archivo_salida:
            resultado_esperado = archivo_salida.readlines()

        resultad_actual = resultado_test.getvalue().strip().split('\n')
        self.assertEqual(len(resultado_esperado), len(resultad_actual))

        for linea_esperada, linea_actual in zip(resultado_esperado, resultad_actual):
            self.assertEqual(linea_esperada.strip(), linea_actual.strip())
