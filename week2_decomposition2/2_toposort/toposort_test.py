from toposort import toposort, to_string, parse_input, is_toposort, from_string
import unittest
import random
import time

MAX_VERTICES = 1000


# TODO: expose instead via "test helpers" from common / DFS lib
def gen_graph(num_vertices=0, has_cycle=False):
    if not num_vertices:
        num_vertices = random.randint(2, MAX_VERTICES)

    adj_list = [None] * num_vertices
    for i in range(num_vertices):
        possible_edges = range(i + 1, num_vertices)
        # only add edges to higher number vertices => no back edges => no cycles
        num_edges = random.randint(0, num_vertices - i - 1)
        adj_list[i] = sorted(random.sample(possible_edges, num_edges))

    if has_cycle:
        back_edge = random.randint(1, num_vertices - 1)
        adj_list[0] = sorted(adj_list[0] + [back_edge])
        adj_list[back_edge] = [0] + adj_list[back_edge]

    return adj_list


class ToposortTest(unittest.TestCase):
    def test_examples(self):
        in1 = """
        4 3
        1 2
        4 1
        3 1
        """
        out1 = "4 3 1 2"
        adj1 = parse_input(in1)
        # verify example from the PDF
        self.assertTrue(is_toposort(adj1, from_string("4 3 1 2")))

        # now find my own toposort
        order1 = toposort(adj1)
        self.assertTrue(is_toposort(adj1, order1))

        # double-check that is_toposort works and returns False for an invalid order
        self.assertFalse(is_toposort(adj1, [1, 2, 3, 4]))

        in2 = """
        4 1
        3 1
        """
        adj2 = parse_input(in2)
        self.assertTrue(is_toposort(adj2, from_string("2 3 1 4")))

        order2 = toposort(adj2)
        self.assertTrue(is_toposort(adj2, order2))

        in3 = """
        5 7
        2 1
        3 2
        3 1
        4 3
        4 1
        5 2
        5 3
        """
        adj3 = parse_input(in3)
        self.assertTrue(is_toposort(adj3, from_string("5 4 3 2 1")))

        order3 = toposort(adj3)
        self.assertTrue(is_toposort(adj3, order3))

    def test_generated(self):
        # for i in range(100): # i in range(100) .. together take ~25s to run
        # i = 200 takes ~7s to run
        for i in range(70):  # i in range(70) .. takes ~7s total to run
            adj = gen_graph(num_vertices=10 * i)
            num_edges = 0
            for a in adj:
                num_edges += len(a)
            print("n={} m={}".format(len(adj), num_edges))
            order = toposort(adj)
            self.assertTrue(is_toposort(adj, order))


if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    random.seed(seed)
    unittest.main()
