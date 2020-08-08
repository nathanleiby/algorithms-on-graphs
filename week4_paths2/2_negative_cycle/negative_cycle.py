# Uses python3

import math
import random
import sys

# relax modifies the distances, if possible
# TODO: refactor with dijkstra?
def relax(adj, cost, distance, prev, loop_check=False):
    # for each vertex
    for v in range(len(adj)):
        # check for shortest path to neighbors
        for idx, neighbor in enumerate(adj[v]):
            c = cost[v][idx]
            relaxed_cost = distance[v] + c
            if relaxed_cost < distance[neighbor]:
                if loop_check:
                    relaxed_cost = (
                        -math.inf
                    )  # there's a negative loop including this vertex
                distance[neighbor] = relaxed_cost
                prev[neighbor] = v


def bellman_ford(adj, cost, s):
    # This algo will give us two results:
    # (1) the shortest path from s to every other vertex
    # (2) whether or not the graph has a negative cycle

    # initialize
    distance = []
    prev = []
    for _ in range(len(adj)):
        distance.append(math.inf)
        prev.append(None)
    distance[s] = 0

    # for |vertex|-1 rounds...
    for _ in range(len(adj) - 1):
        relax(adj, cost, distance, prev)

    # one more relax, to check for cycles
    relax(adj, cost, distance, prev, loop_check=True)

    # Check if any vertex is part of a negative cycle
    if -math.inf in distance:
        d = distance.index(-math.inf)
        # now that we've found a single node that's part of a negative cycle,
        # we need to figure out the remaining nodes
        #
        # From lecture notes...
        #  Start from x ← v, follow the link
        #  x ← prev[x] for |V | times — will be
        #  definitely on the cycle
        cur = d
        for _ in range(len(adj)):
            # step back one node
            cur = prev[cur]
            distance[cur] = -math.inf
            if cur == d:
                break

    return distance, prev


# return 1 if graph has negative cycle and 0 if not
def negative_cycle(adj, cost):
    # doesn't matter what starting node we choose,
    # as long as graph is one connected component
    vertices = list(range(len(adj)))
    start_v = random.choice(vertices)

    distance, _ = bellman_ford(adj, cost, start_v)
    has_negative_cycle = -math.inf in distance

    return int(has_negative_cycle)


def parse_input(text):
    data = list(map(int, text.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3])
    )
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    return adj, cost


if __name__ == "__main__":
    print(*parse_input(sys.stdin.read()))
