from connected_components import number_of_components, parse_input
import unittest
import random
import time

in1 = """
4 2
1 2
3 2
"""
out1 = 2

# EDGE CASES
# - no edges in graph


MAX_SIZE = 1000


def gen_graph():
    num_v = random.randint(2, MAX_SIZE)
    edges = []

    vertices = range(1, num_v + 1)
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
    chosen_splits = []
    split_idxs = range(1, num_v)
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
    # Create fully connected components
    for c in components:
        for i in range(len(c)):
            for j in range(i + 1, len(c)):
                edges.append((c[i], c[j]))

    # print("Edges:\n", edges)

    return num_v, edges, num_components


def graph_to_string(num_v, edges):
    out = "{} {}\n".format(num_v, len(edges))

    for e in edges:
        out += "{} {}\n".format(e[0], e[1])

    return out


class TestConnectedComponents(unittest.TestCase):
    def test_all(self):
        for spec in [
            dict(input=in1, output=out1),
            # dict(input=in2, output=out2),
        ]:
            actual = number_of_components(parse_input(spec["input"]))
            expected = spec["output"]
            self.assertEqual(actual, expected)

    def test_generated_graphs(self):
        print("\n")
        for i in range(100):
            has_path = random.choice([True, False])
            num_v, edges, expected = gen_graph()
            print(
                "graph {:03} (num_components= {:4}, num_v = {:4}, num_e = {:7}) ... ".format(
                    i, expected, num_v, len(edges)
                )
            ),
            generated_input = graph_to_string(num_v, edges)
            # print(generated_input)
            adj = parse_input(generated_input)
            t_before = time.time()
            actual = number_of_components(adj)
            duration = time.time() - t_before
            print("\tduration = {}".format(duration))

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    seed = time.time()
    print("Random Seed = ", seed)
    random.seed(seed)
    unittest.main()
