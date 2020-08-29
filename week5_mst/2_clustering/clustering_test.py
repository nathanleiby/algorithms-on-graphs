from clustering import clustering, parse_input

import unittest
import random
import time
import math

in1 = """
12
7 6
4 3
5 1
1 7
2 7
5 7
3 3
7 8
2 8
4 4
6 7
2 6
3
"""
out1 = round(2.828427124746, 7)

in2 = """
8
3 1
1 2
4 6
9 8
9 9
8 9
3 11
4 12
4
"""
out2 = round(5.000000000, 7)

# TODO: Try running some tests at scale.
# 1 ≤ 𝑛 ≤ 200; −10**3 ≤ 𝑥𝑖, 𝑦𝑖 ≤ 10**3 are integers.


class Test(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(clustering(*parse_input(in1)), out1)
        self.assertEqual(clustering(*parse_input(in2)), out2)


if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    random.seed(seed)
    unittest.main()
