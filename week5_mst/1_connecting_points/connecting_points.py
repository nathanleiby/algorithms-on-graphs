# Uses python3
import sys
import math
import random


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def build_graph(x, y):
    # build the graph -- create the nodes and edge lengths
    # it's a fully connected graph
    vertices = []
    for idx in range(len(x)):
        pt = (x[idx], y[idx])
        vertices.append(pt)

    # initialize adjacent-list representation and costs
    adj = []
    costs = []
    for _ in range(len(vertices)):
        adj.append([])
        costs.append([])

    # 0: 1 2 3
    # 1:   2 3
    # 2:     3
    # TODO: What's the right representation for the graph, when
    # doing Prim's / Kruskal's?
    # This is the first problem where we had to build the graph
    # vs just getting it in adjacency list format.
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            src = vertices[i]
            dst = vertices[j]
            adj[i].append(j)
            costs[i].append(euclidean_distance(src, dst))

    return adj, costs


def mst(adj, costs, algo="prim"):
    if algo == "prim":
        return prim(adj, costs)
    else:
        return kruskal(adj, costs)


def _get_lightest_edge(adj, costs, mst_v):
    """ Gets the lightest edge to a new vertex,
        i.e thats not yet in the mst you're building """
    # TODO: Replace with a heap / priority queue for performance
    min_cost = math.inf
    min_edge = None
    for src, edges in enumerate(adj):
        for d_idx, dst in enumerate(edges):
            # we want an edge that connects the existing tree to a new vertex...
            if src in mst_v and dst in mst_v:
                # both already in tree
                continue
            if (src not in mst_v) and (dst not in mst_v):
                # neither already in tree
                continue

            edge_cost = costs[src][d_idx]
            if edge_cost < min_cost:
                min_cost = edge_cost
                min_edge = (src, dst)

    return min_edge, min_cost


def prim(adj, costs):
    # TODO: Return the list of edges instead, and compute cost externally
    # "repeatedly attach a new vertex to the tree by the lightest edge"
    mst_v = set()
    mst_e = set()
    total_cost = 0

    # initialize with a random starting vertex
    v_idx = random.choice(range(len(adj)))
    mst_v = set(iter([v_idx]))

    while len(mst_v) < len(adj):
        edge, cost = _get_lightest_edge(adj, costs, mst_v)
        mst_v.add(edge[0])
        mst_v.add(edge[1])
        mst_e.add(edge)
        total_cost += cost

    return total_cost, mst_e


def kruskal(adj, costs):
    # "repeatedly add the next lightest edge that doesn't produce a cycle"
    # TODO: Also implement Kruskal
    return []


def minimum_distance(x, y):
    adj, costs = build_graph(x, y)
    total_cost, _ = mst(adj, costs)
    return round(total_cost, 9)


def parse_input(text):
    data = list(map(int, text.split()))
    x = data[1::2]
    y = data[2::2]
    return x, y


if __name__ == "__main__":
    x, y = parse_input(sys.stdin.read())
    print("{0:.9f}".format(minimum_distance(x, y)))
