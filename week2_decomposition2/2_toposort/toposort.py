#Uses python3

import sys
import dfs
import copy

def toposort(adj):
    # print("adj:\n", adj)
    bookkeeping = dfs.dfs2(adj)

    # print("pre-visit:      ", bookkeeping['previsit'])
    # print("post-visit:     ", bookkeeping['postvisit'])
    pv = copy.copy(bookkeeping['postvisit'])
    pv_to_v = zip(pv, range(len(pv))) # map from postvisit to vertex id
    pv_to_v = sorted(pv_to_v, key=lambda x: x[0], reverse=True) # sort (reverse) by postvisit

    order = list(map(lambda x: x[1], pv_to_v))
    return order

# TODO: idea... verify_toposort()
# for a given output of toposort().. visit in order and makes each one you visit DOES NOT point back to an unvisited node
def is_toposort(adj, order):
    visited = [False] * len(adj)
    for o in order:
        # it should not have any inbound edges from an unvisited node
        for v, edges in enumerate(adj):
            if not visited[v] and o in edges:
                return False
        visited[o] = True

    return True


def to_string(order):
    # stringifies the output, as expected
    add_one = list(map(lambda x: str(x + 1), order))
    return " ".join(add_one)

def from_string(order_s):
    order_list = order_s.split(" ")
    sub_one = list(map(lambda x: int(x) - 1, order_list))
    return sub_one


def parse_input(input):
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    return adj


if __name__ == '__main__':
    adj = parse_input(sys.stdin.read())
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

