import unittest

class TestMyClass(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
