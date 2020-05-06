#Uses python3

import sys


class HasCycleException(Exception):
    pass

def acyclic(adj):
    try:
        dfs(adj)
    except HasCycleException as e:
        print(e)
        return 1
    return 0

def dfs(adj):
    """ dfs does a depth-first-search """
    visited = [False] * len(adj)
    for v in range(len(adj)):
        if visited[v]:
            continue
        explore(adj, visited, v, [v])

    # we should have visited every vertex
    assert(all(visited))

def explore(adj, visited, v, stack):
    """ explore all vertices that can be reached from v, marking them as visited """
    visited[v] = True
    for neighbor in adj[v]:
        if neighbor in stack:
            # error if we find a back-edge, which indicates a cycle in a DAG
            raise HasCycleException("Cycle found where {} has back-edge to {}".format(v, neighbor))
        if not visited[neighbor]:
            explore(adj, visited, neighbor, stack + [neighbor])

    # we should have visited all neighbors of this vertex
    assert(neighbor in visited for neighbor in adj[v])

def parse_input(text):
    data = list(map(int, text.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    return adj

if __name__ == '__main__':
    text = sys.stdin.read()
    adj = parse_input(text)
    print(acyclic(adj))
