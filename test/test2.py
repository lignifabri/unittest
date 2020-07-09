import unittest

class Otros_test(unittest.TestCase):

    @unittest.skip("no se ejecuta")
    def test_otra_suma(self):
        self.assertEqual(2+2,4)

    def test_otra_resta(self):
        self.assertEqual(2-2,0)


# if __name__=='__main__':
    # unittest.main()
