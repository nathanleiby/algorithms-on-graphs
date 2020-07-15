from negative_cycle import negative_cycle, parse_input

import unittest
import random
import time

in1 = """
4 4
1 2 -5
4 1 2
2 3 2
3 1 1
"""
out1 = 1

# Only 1 sample above was given in PDF
# Making up some others quickly..

# Here's a quick variation that won't have a negative cycle, because no negative edges
in2 = """
4 4
1 2 5
4 1 2
2 3 2
3 1 1
"""
out2 = 0

# Here's another variation that won't have a negative cycle, because negative edge weight is too small
in3 = """
4 4
1 2 -1
4 1 2
2 3 2
3 1 1
"""
out3 = 0


class Test(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(negative_cycle(*parse_input(in1)), out1)
        self.assertEqual(negative_cycle(*parse_input(in2)), out2)
        self.assertEqual(negative_cycle(*parse_input(in3)), out3)


if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    random.seed(seed)
    unittest.main()
