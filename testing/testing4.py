import unittest


class TestStuff(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1+1, 2)

    def test_subtraction(self):
        self.assertEqual(1-1, 0)

    @unittest.skip('to be implemented')
    def test_multiplication(self):  
        pass


if __name__=='__main__':
    unittest.main()