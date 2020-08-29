# Uses python3
import sys
import math
from connecting_points import build_graph, mst

def get_edge_cost(adj, costs, e):
    src, dst = e[0], e[1]
    edges_from_src = adj[src]
    dst_idx = edges_from_src.index(dst)

    return costs[src][dst_idx]

def clustering(x, y, k):
    """
    @param x: the x-coords of the points
    @param y: the y-coords of the points
    @param k: number of non-empty subsets (clusters)
    """


    # make a graph
    adj, costs = build_graph(x, y)

    # create an MST from the graph
    _, edges = mst(adj, costs)

    # sort the edges by decreasing weight
    print("EDGE COSTS")
    ecosts =list(map(lambda e: get_edge_cost(adj, costs, e), edges))
    ecosts_sorted = list(sorted(list(ecosts), reverse=True))
    print(ecosts_sorted)

    # largest possible distance is length of the (k-1)th edge.
    #
    # if you cut out (k-1) edges, you'll divide graph into (k)
    # non-empty connected components.
    c = ecosts_sorted[(k-1)-1] # other (-1) is to handle 0-indexing of array
    return round(c, 7) # answer expected at this precision level

def parse_input(input):
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0 : 2 * n : 2]
    y = data[1 : 2 * n : 2]
    data = data[2 * n :]
    k = data[0]
    return x,y,k

if __name__ == "__main__":
    input = sys.stdin.read()
    print("{0:.9f}".format(clustering(*parse_input(input))))
