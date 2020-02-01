import unittest
from random import randint

from tqdm import trange

from sort import sort_algorithms


class SortTest(unittest.TestCase):

    def test_sort(self):
        for _ in trange(1000):
            random_list = [randint(-100, 300) for _ in range(randint(0, 500))]
            right = sorted(random_list)
            for func in sort_algorithms:
                self.assertEqual(right, func(random_list), str(random_list))


if __name__ == '__main__':
    unittest.main()
