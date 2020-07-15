# Uses python3

import math
import sys

from negative_cycle import bellman_ford

# returns an array of distances to each vertex from s
#
# if not reachable, distance=math.inf
# if not shortest path, distance=-math.inf
def shortest_paths(adj, cost, s):
    distance, _ = bellman_ford(adj, cost, s)
    return distance


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
    s = data[0]
    s -= 1
    return adj, cost, s


if __name__ == "__main__":
    adj, cost, s = parse_input(sys.stdin.read())
    out = shortest_paths(adj, cost, s)
    for x in out:
        if x == math.inf:
            # not reachable
            print("*")
        elif x == -math.inf:
            # no shortest path (b/c inf loop)
            print("-")
        else:
            # path length
            print(x)
