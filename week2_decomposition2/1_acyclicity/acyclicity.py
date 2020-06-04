# Uses python3

import sys
import dfs


def acyclic(adj, version=2):
    try:
        if version == 2:
            dfs.dfs2(adj)
        else:
            dfs.dfs(adj)
    except dfs.HasCycleException as e:
        # print(e)
        return 1
    return 0


def parse_input(text):
    data = list(map(int, text.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    return adj


if __name__ == "__main__":
    text = sys.stdin.read()
    adj = parse_input(text)
    print(acyclic(adj))
