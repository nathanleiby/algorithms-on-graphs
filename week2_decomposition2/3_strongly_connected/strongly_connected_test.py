from strongly_connected import (
    number_of_strongly_connected_components,
    parse_input,
    reverse_graph,
)
import unittest
import random
import time

# TODO: expose instead via "test helpers" from common / DFS lib
MAX_SIZE = 1000


def gen_graph():
    # Generates a graph with `s` strongly connected components, where `s <= n` (n = number of verticies)
    # 1. make a list of verticies
    # 2. determine # of SCCs
    # 3. split list of vertices into <result of (2)> subgroups
    # 4. for each subgroup, draw a simple cycle (e.g. 1 => 2 => 3 => 1)

    num_v = random.randint(2, MAX_SIZE)
    edges = []

    vertices = list(range(1, num_v + 1))
    random.shuffle(vertices)

    # 1 is fully connected, num_v would be no edges
    num_components = random.randint(1, num_v)

    # chooses a number of locations in which to split up the vertices
    # Suppose 5 vertices and two splits
    # If:
    #   Vertices     = [ 4, 2, 3, 5, 1 ]   # NOTE: These are shuffled
    #   Split Idxs   = [ 1, 4 ]            # These are the indices to split before
    # Then:
    #   Components = [4], [2,3,5], [1]
    split_idxs = list(range(1, num_v))
    random.shuffle(split_idxs)
    chosen_split_idxs = split_idxs[: num_components - 1]
    chosen_split_idxs.sort()

    components = []
    prev = 0
    for c in chosen_split_idxs:
        components.append(vertices[prev:c])
        prev = c
    components.append(vertices[prev:])
    # print("Num components", num_components)
    # print("Components: ", components)

    edges = []
    # Create strongly connected components
    for c in components:
        for i in range(len(c)):
            e = (c[i - 1], c[i])
            edges.append(e)

    # print("Edges:\n", edges)

    return num_v, edges, num_components


def graph_to_string(num_v, edges):
    out = "{} {}\n".format(num_v, len(edges))

    for e in edges:
        out += "{} {}\n".format(e[0], e[1])

    return out


class ToposortTest(unittest.TestCase):
    def test_examples(self):
        in1 = parse_input(
            """
4 4
1 2
4 1
2 3
3 1
"""
        )
        self.assertEqual(number_of_strongly_connected_components(in1), 2)

        in2 = parse_input(
            """
5 7
2 1
3 2
3 1
4 3
4 1
5 2
5 3
"""
        )
        self.assertEqual(number_of_strongly_connected_components(in2), 5)

    def test_generated(self):
        for i in range(10):
            num_v, edges, num_components = gen_graph()
            print(
                "graph {:03} (num_components= {:4}, num_v = {:4}, num_e = {:7}) ... ".format(
                    i, num_components, num_v, len(edges)
                )
            ),
            generated_input = graph_to_string(num_v, edges)
            adj = parse_input(generated_input)
            t_before = time.time()
            actual = number_of_strongly_connected_components(adj)
            duration = time.time() - t_before
            print("\tduration = {}".format(duration))
            self.assertEqual(actual, num_components)


if __name__ == "__main__":
    seed = time.time()
    print("random seed = ", seed)
    # seed = 1589097718.744887
    # print("OVERRIDE", seed)
    random.seed(seed)
    unittest.main()
