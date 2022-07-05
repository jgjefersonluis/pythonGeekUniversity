import unittest
from logging import Logger
from sqlalchemy import null


class AnalizadorTest(unittest.TestCase):
        def setUp(self):
                self.analizador = Logger.analizador

        def test_nome_arquivo_log_valido_letras_maiusculas(self, analizador=None):
                resultado = analizador.nome_arquio_log_valido("log_salvo.LOG")
                self.assertTrue(resultado)

        def test_nome_arquivo_log_valido_letras_minusculas(self):
                resultado = self.analizador.nome_arquio_log_valido("log_salvo.log")
                self.assertTrue(resultado)

        def tearDown(self):
                self.analizador = null
                