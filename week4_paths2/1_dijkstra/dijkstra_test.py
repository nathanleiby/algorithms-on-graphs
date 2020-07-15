from dijkstra import parse_input, distance
import unittest
import random
import time

in1 = """
4 4
1 2 1
4 1 2
2 3 2
1 3 5
1 3
"""
out1 = 3

in2 = """
5 9
1 2 4
1 3 2
2 3 2
3 2 1
2 4 2
3 5 4
5 4 1
2 5 3
3 4 4
1 5
"""
out2 = 6

in3 = """
3 3
1 2 7
1 3 5
2 3 2
3 2
"""
out3 = -1


class Test(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(distance(*parse_input(in1)), out1)
        self.assertEqual(distance(*parse_input(in2)), out2)
        self.assertEqual(distance(*parse_input(in3)), out3)


if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    random.seed(seed)
    unittest.main()
