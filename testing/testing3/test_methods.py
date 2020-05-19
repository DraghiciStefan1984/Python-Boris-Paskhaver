import unittest
import methods

class TestMethods(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(methods.multiply(3, 4), 12)

    
if __name__=='__main__':
    unittest.main()