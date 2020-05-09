from toposort import toposort, to_string, parse_input
import unittest
import random
import time

MAX_VERTICES = 1000


# TODO: Add to test helpers
# def gen_graph(num_vertices=0, has_cycle=False):
#     if not num_vertices:
#         num_vertices = random.randint(2, MAX_VERTICES)

#     adj_list = [None] * num_vertices
#     for i in range(num_vertices):
#         possible_edges = range(i + 1, num_vertices)
#         # only add edges to higher number vertices => no back edges => no cycles
#         num_edges = random.randint(0, num_vertices - i - 1)
#         adj_list[i] = sorted(random.sample(possible_edges, num_edges))

#     if has_cycle:
#         back_edge = random.randint(1, num_vertices - 1)
#         adj_list[0] = sorted(adj_list[0] + [back_edge])
#         adj_list[back_edge] = [0] + adj_list[back_edge]

#     return adj_list


class AcyclicityTest(unittest.TestCase):
    def test_examples(self):
        in1 = """
        4 3
        1 2
        4 1
        3 1
        """
        out1 = "4 3 1 2"
        adj1 = parse_input(in1)
        self.assertEqual(to_string(toposort(adj1)), out1)

        in2 = """
        4 1
        3 1
        """
        # out2 = "2 3 1 4" # this is ONE valid order, but there are many..
        out2 = "4 3 2 1"
        adj2 = parse_input(in2)
        self.assertEqual(to_string(toposort(adj2)), out2)

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
        out3 = "5 4 3 2 1"
        adj3 = parse_input(in3)
        self.assertEqual(to_string(toposort(adj3)), out3)


    # def test_generated(self):
    #     for i in range(100):
    #         adj = gen_graph(num_vertices=10 * i)
    #         self.assertEqual(acyclic(adj), 0)
    #     for i in range(100):
    #         adj = gen_graph(num_vertices=10 * i, has_cycle=True)
    #         # print(adj)
    #         self.assertEqual(acyclic(adj), 1)


if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    random.seed(seed)
    unittest.main()
