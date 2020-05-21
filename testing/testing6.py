import unittest


class TestOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('run before every test suite')

    @classmethod
    def tearDownClass(cls):
        print('run after every test suite')

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])

if __name__=='__main__':
    unittest.main()