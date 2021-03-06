# Uses python3

import sys


def reach(adj, x, y):
    # do depth first search on an adjacency list
    visited = {}
    to_visit = [x]
    while len(to_visit) > 0:
        cur = to_visit.pop()
        visited[cur] = True
        if cur == y:  # found
            return 1
        neighbors = adj[cur]
        unvisited_neighbors = filter(lambda x: x not in visited, neighbors)
        to_visit.extend(unvisited_neighbors)

    return 0


def parse_input(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    x, y = data[2 * m :]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return adj, x, y


if __name__ == "__main__":
    # read from stdin
    adj, x, y = parse_input(sys.stdin.read())
    print(reach(adj, x, y))
