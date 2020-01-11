import unittest

from sort import sort_algorithms


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(len(sort_algorithms), 2)


if __name__ == '__main__':
    unittest.main()
