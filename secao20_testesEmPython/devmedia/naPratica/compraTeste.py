import unittest
from compra import Compra

class CompraTeste(unittest.TestCase):
    def test_frete_gratis(self):
        nova_compra = Compra()
        assert nova_compra.frete_gratis(100), "erro em Compra.frete_gratis"

    if __name__ == "__main__":
        unittest.main()