from acyclicity import parse_input, acyclic
import unittest

in1 = """
4 4
1 2
4 1
2 3
3 1
"""

in2 = """
5 7
1 2
2 3
1 3
3 4
1 4
2 5
3 5
"""

class AcyclicityTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(acyclic(parse_input(in1)), 1)
        self.assertEqual(acyclic(parse_input(in2)), 0)

if __name__ == "__main__":
    unittest.main()