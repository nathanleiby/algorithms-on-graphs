from strongly_connected import number_of_strongly_connected_components, parse_input, reverse_graph
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
        in1 = parse_input("""
4 4
1 2
4 1
2 3
3 1
""")
        self.assertEqual(number_of_strongly_connected_components(in1), 2)

        in2= parse_input("""
5 7
2 1
3 2
3 1
4 3
4 1
5 2
5 3
""")
        self.assertEqual(number_of_strongly_connected_components(in2), 5)



if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    # seed = 1589097718.744887
    # print("OVERRIDE", seed)
    random.seed(seed)
    unittest.main()
