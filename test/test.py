import unittest

class Mis_test(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(2+2,4)
    
    def test_resta(self):
        self.assertTrue(1-1==0)

if __name__=='__main__':
    unittest.main()
