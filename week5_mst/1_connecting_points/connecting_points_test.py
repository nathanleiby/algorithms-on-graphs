from connecting_points import minimum_distance, parse_input

import unittest
import random
import time
import math

in1 = """
4
0 0
0 1
1 0
1 1
"""
out1 = 3

in2 = """
5
0 0
0 2
1 1
3 0
3 2
"""
out2 = 7.064495102

# TODO: Try running some tests at scale.
# 1 ≤ 𝑛 ≤ 200; −10**3 ≤ 𝑥𝑖, 𝑦𝑖 ≤ 10**3 are integers.


class Test(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_distance(*parse_input(in1)), out1)
        self.assertEqual(minimum_distance(*parse_input(in2)), out2)


if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    random.seed(seed)
    unittest.main()
