from reachability import parse_input, reach
import unittest
import random
import time

in1 = """
4 4
1 2
3 2
4 3
1 4
1 4
"""
out1 = 1

in2 = """
4 2
1 2
3 2
1 4
"""
out2 = 0

MAX_SIZE = 999


def gen_graph(p_edge=0.5, has_path=True):
    num_v = random.randint(2, MAX_SIZE)
    edges = []

    # what are the start and end vertices of the path we're checking for?
    start = random.randint(1, num_v)
    end = start
    while start == end:
        # make sure end != start
        end = random.randint(1, num_v)

    for i in range(1, num_v + 1):
        if not has_path and i == end:
            # if there's NO path, don't create any edge from 'end'
            continue

        for j in range(i + 1, num_v + 1):
            if not has_path and j == end:
                # if there's NO path, don't create any edge to 'end'
                continue

            if random.random() > p_edge:
                edges.append((i, j))

    if has_path:
        # ensure there's a path from start to end
        len_path = random.randint(1, num_v - 1)

        vertices = list(range(1, num_v + 1))
        vertices.remove(end)
        vertices.remove(start)
        random.shuffle(vertices)

        cur = start
        while len_path > 0:
            if len_path > 1:
                # if it's an intermediate step, connect something other than the end vertex
                nxt = vertices.pop()
            else:
                # it's the last step, so connect to end
                nxt = end
            edges.append((cur, nxt))
            cur = nxt
            len_path -= 1

    deduped_edges = list(set(edges))

    return num_v, deduped_edges, start, end, has_path


def graph_to_string(num_v, edges, start, end):
    out = "{} {}\n".format(num_v, len(edges))

    for e in edges:
        out += "{} {}\n".format(e[0], e[1])

    # path that exists
    out += "{} {}".format(start, end)
    return out


class TestReachability(unittest.TestCase):
    def test_all(self):
        for spec in [
            dict(input=in1, output=out1),
            dict(input=in2, output=out2),
        ]:
            adj, x, y = parse_input(spec["input"])
            actual = reach(adj, x, y)
            expected = spec["output"]
            self.assertEqual(actual, expected)

    def test_generated_graphs(self):
        print("\n")
        for i in range(100):
            p_edge = random.random()  # random [0,1]
            has_path = random.choice([True, False])
            num_v, edges, start, end, _ = gen_graph(p_edge, has_path)
            print(
                "graph {:03} (has_path = {:1}, p_edge = {:.02f}, num_v = {:4}, num_e = {:7})".format(
                    i, has_path, p_edge, num_v, len(edges)
                )
            )
            generated_input = graph_to_string(num_v, edges, start, end)
            # print(generated_input)
            adj, x, y = parse_input(generated_input)
            actual = reach(adj, x, y)
            self.assertEqual(actual, has_path)


if __name__ == "__main__":
    seed = time.time()
    print("Random Seed = ", seed)
    random.seed(seed)
    unittest.main()
