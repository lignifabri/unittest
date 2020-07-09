import unittest



class Mis_test(unittest.TestCase):

    term_uno=0
    term_dos=0
    correr=True

    def setUp(self):
        self.term_uno = 2
        self.term_dos = 2
        if self.term_uno * self.term_dos == 2000:
            self.correr = False

    def test_suma(self):
        self.assertEqual(self.term_uno+self.term_dos,4)
        self.assertTrue(self.correr)

    def test_resta(self):
        self.assertTrue(self.term_uno-self.term_dos==0)
        self.assertTrue(self.correr)

    def test_verificar_iguales(self):
        a=5
        b=4+1
        self.assertEqual(a,b)

    def test_verificar_no_iguales(self):
        a=19
        b=5*3
        self.assertNotEqual(a,b,"a tiene que ser diferente de b")

    def tearDown(self):
        print('Borrando datos.......')

if __name__=='__main__':
    unittest.main()
