from secao20_testesEmPython.devmedia.naPratica.compra import Compra


def test_frete_gratis_exception(self):
    nova_compra = Compra()
    self.assertRaises(TypeError, nova_compra.frete_gratis, "duzentos")