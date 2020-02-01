import unittest
from random import randint

from tqdm import trange

from tree.BinaryIndexTree import BinaryIndexTree


class TreeTest(unittest.TestCase):

    def test_BIT(self):
        for _ in trange(1000):
            random_list = [randint(-100, 300) for _ in range(randint(1, 100))]
            BIT = BinaryIndexTree(random_list)
            for _ in range(100):
                idx = randint(0, len(random_list) - 1)
                val = randint(-100, 300)
                random_list[idx] = val
                BIT.update(idx, val)
                for i in range(len(random_list)):
                    self.assertEqual(BIT.query(0, i), sum(random_list[:i]))


if __name__ == '__main__':
    unittest.main()
