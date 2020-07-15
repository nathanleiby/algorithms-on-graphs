from bfs import parse_input, distance
import unittest
import random
import time

in1 = """
4 4
1 2
4 1
2 3
3 1
2 4
"""
out1 = 2

in2 = """
5 4
5 2
1 3
3 4
1 4
3 5
"""
out2 = -1

# MAX_VERTICES = 1000


def gen_graph(num_vertices=0, path_length=5, s=0, t=0):
    adj_list = [[] for _ in range(num_vertices)]

    vertices = range(num_vertices)
    intermediate_items = list(filter(lambda x: x != s and x != t, vertices))
    random.shuffle(intermediate_items)

    path_items = random.sample(set(intermediate_items), path_length - 1)
    print("path items", path_items)

    prev = s
    for nxt in path_items:
        print("nxt = ", nxt)
        adj_list[prev] = [nxt]
        l = adj_list[prev]
        print("l = ", l)
        # l.append(nxt)
        # [ [ ], [ ], [ ]]
        prev = nxt

    # TODO: Another approach... assign every node to a distance, and then draw
    # connections from layer (n-1) to layer (n)
    #
    # It's also possible

    adj_list[prev].append(t)

    return adj_list


class Test(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(distance(*parse_input(in1)), out1)
        self.assertEqual(distance(*parse_input(in2)), out2)

    def test_generated(self):
        # for i in range(10, 100):
        for i in range(10, 12):
            expected = 5
            adj = gen_graph(num_vertices=i, path_length=expected, s=0, t=i - 1)
            self.assertEqual(distance(adj, 0, i - 1), expected)

        # for i in range(100):
        #     adj = gen_graph(num_vertices=10 * i, has_cycle=True)
        #     # print(adj)
        #     self.assertEqual(acyclic(adj), 1)


if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    random.seed(seed)
    unittest.main()
