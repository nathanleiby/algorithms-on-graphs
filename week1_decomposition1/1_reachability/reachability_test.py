from reachability import parse_input, reach
import unittest

in1 = """4 4
1 2
3 2
4 3
1 4
1 4
"""

out1 = 1

class TestReachability(unittest.TestCase):
    def test_all(self):
        for spec in [
            dict(input=in1, output=out1),
        ]:
            adj, x, y = parse_input(spec['input'])
            actual = reach(adj, x, y)
            expected = spec['output']
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()