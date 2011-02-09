import unittest
from functional_test import *

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFunctional))
    unittest.TextTestRunner().run(suite)