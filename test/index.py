import unittest

import test
import test2

if __name__=='__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test))
    suite.addTests(loader.loadTestsFromModule(test2))
    runner = unittest.TextTestRunner(verbosity=3)
    results = runner.run(suite)

    # unittest.main()
