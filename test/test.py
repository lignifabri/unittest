import unittest
import platform

class Mis_test(unittest.TestCase):

    term_uno=0
    term_dos=0
    correr=True

    def setUp(self):
        self.term_uno = 2
        self.term_dos = 2
        if self.term_uno * self.term_dos == 2000:
            self.correr = False

    @unittest.skip("No se ejecuta porque necesita cambios")
    def test_suma(self):
        self.assertEqual(self.term_uno+self.term_dos,4)
        self.assertTrue(self.correr)

    @unittest.skip("No necesita verificación por cambio de funcionalidad")
    def test_resta(self):
        self.assertTrue(self.term_uno-self.term_dos==0)
        self.assertTrue(self.correr)

    @unittest.skipIf(platform.system()=='Linux',"no se ejecuta en Linux")
    def test_verificar_iguales(self):
        a=5
        b=4+1
        #verufica a==b
        self.assertEqual(a,b)

    @unittest.skipUnless(platform.system()=='Linux',"Sólo se ejecuta en Linux")
    def test_verificar_no_iguales(self):
        a=19
        b=5*3
        #verifica a!=b
        self.assertNotEqual(a,b,"a tiene que ser diferente de b")

    def test_validar_si_verdadero(self):
        a=2
        self.assertTrue(a==2,"Esperaba un true")

    def test_validar_si_falso(self):
        a=5
        self.assertFalse(a==2+4,"Esperaba un false")

    def test_es_nulo(self):
        a=None
        self.assertIsNone(a,"Se espera que a sea nulo")

    def test_no_es_nulo(self):
        a=0
        self.assertIsNotNone(a,"Se espea que a no sea nulo")

    def test_es(self):
        a=5
        b=5
        self.assertIs(a,b,"No son iguales")

    def test_no_es(self):
        a=5
        b=5.00
        self.assertIsNot(a,b,"Son iguales")

    def test_texto_en(self):
        a="Hola"
        b="Hola Mundo"
        self.assertIn(a,b,"No está dentro")

    def test_texto_no_en(self):
        a="hola"
        b="Hola Mundo"
        self.assertNotIn(a,b,"El texto está incluido")

    def test_es_mayor(self):
        a=7
        b=5
        self.assertGreater(a,b,"A tiene que ser mayor que B")

    def test_es_mayor_igual(self):
        a=5
        b=5
        self.assertGreaterEqual(a,b,"A debe ser mayor o igual a B")

    def test_es_menor(self):
        a=3
        b=5
        self.assertLess(a,b,"A tiene que ser menor a B")

    def test_es_menot_igual(self):
        a=3
        b=3
        self.assertLessEqual(a,b,"A tiene que ser menor o igual a B")


    def tearDown(self):
        print('Borrando datos.......')

if __name__=='__main__':
    unittest.main()





