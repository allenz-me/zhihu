import unittest
from random import randint
from tqdm import trange
from algorithms import inversion

class AlgorithmTest(unittest.TestCase):

    def test_inversions(self):
        for _ in trange(1000):
            random_list = [randint(-100, 500) for _ in range(randint(0, 1000))]
            right = inversion.inversions_brute(random_list)
            self.assertEqual(inversion.inversions_merge(random_list)[1],
                             right)
            self.assertEqual(inversion.inversions_bisect(random_list),
                             right)
            self.assertEqual(inversion.inversion_bit(random_list),
                             right)


if __name__ == '__main__':
    unittest.main()
