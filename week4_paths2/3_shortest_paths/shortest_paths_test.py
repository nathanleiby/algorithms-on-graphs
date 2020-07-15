from shortest_paths import shortest_paths, parse_input

import unittest
import random
import time
import math

in1 = """
6 7
1 2 10
2 3 5
1 3 100
3 5 7
5 4 10
4 3 -18
6 1 -1
1
"""
out1 = [0, 10, -math.inf, -math.inf, -math.inf, math.inf]

# Only 1 sample above was given in PDF
# Making up some others quickly..

# Here's a quick variation that won't have a negative cycle, because no negative edges
in2 = """
5 4
1 2 1
4 1 2
2 3 2
3 1 -5
4
"""
out2 = [-math.inf, -math.inf, -math.inf, 0, math.inf]


class Test(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(shortest_paths(*parse_input(in1)), out1)
        self.assertEqual(shortest_paths(*parse_input(in2)), out2)


if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    random.seed(seed)
    unittest.main()
