from connected_components import number_of_components, parse_input
import unittest

in1 = """
4 2
1 2
3 2
"""
out1 = 2


class TestConnectedComponents(unittest.TestCase):
    def test_all(self):
        for spec in [
            dict(input=in1, output=out1),
            # dict(input=in2, output=out2),
        ]:
            actual = number_of_components(parse_input(spec['input']))
            expected = spec['output']
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()