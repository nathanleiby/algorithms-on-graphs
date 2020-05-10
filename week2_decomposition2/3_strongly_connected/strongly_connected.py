#Uses python3

import sys
import dfs

sys.setrecursionlimit(200000)

## --------------------
# COPIED FROM toposort.py
import copy
def toposort(adj):
    """ returns list of vertices in descending post-visit order """
    # print("adj:\n", adj)
    bookkeeping = dfs.dfs2(adj, err_on_cycle=False)

    # print("pre-visit:      ", bookkeeping['previsit'])
    # print("post-visit:     ", bookkeeping['postvisit'])
    pv = copy.copy(bookkeeping['postvisit'])
    pv_to_v = zip(pv, range(len(pv))) # map from postvisit to vertex id
    pv_to_v = sorted(pv_to_v, key=lambda x: x[0], reverse=True) # sort (reverse) by postvisit

    order = list(map(lambda x: x[1], pv_to_v))
    return order
## --------------------

def number_of_strongly_connected_components(adj):
    # do DFS on the reverse graph
    adj_r = reverse_graph(adj)
    order = toposort(adj_r) 

    ## -------------
    # TODO: TLDR Don't use toposort, b/c we cant toposort a non-DAG (!) but SCCs are only of interest in a non-DAG to create the meta-graph (a DAG)
    def is_toposort(adj, order):
        visited = [False] * len(adj)
        for o in order:
            # it should not have any inbound edges from an unvisited node
            for v, edges in enumerate(adj):
                if not visited[v] and o in edges:
                    return False
            visited[o] = True

        return True
    ## -------------


    print("is_toposort = ", is_toposort(adj_r, order))
    print("Order:")
    print(order)

    bk = dfs.new_bookkeeping(adj)
    sccs = [] 
    # for each v in in G_r in descending post-visit order... (source in G_r <=> sink in G)
    for v in order:
        if bk['visited'][v]:
            continue
        # dfs original graph
        dfs.explore2(adj, v, bookkeeping=bk, err_on_cycle=False)
        # add any newly visited nodes to a new SCC
        new_scc = []
        previously_visited = []
        for s in sccs:
            previously_visited += s
        for v, is_visited in enumerate(bk['visited']):
            if is_visited and not v in previously_visited:
                new_scc.append(v)
        sccs.append(new_scc)

    print("Sccs:")
    print(sccs)
    print("")
    return len(sccs)

def reverse_graph(adj):
    print("reverse_graph")
    print("ADJ:")
    print(adj)

    adj_r = []
    for _ in range(len(adj)):
        adj_r.append([])

    for v in range(len(adj)):
        edges = adj[v]
        for e in edges:
            adj_r[e] += [v]

    print("ADJ_R:")
    print(adj_r)

    return adj_r

# TODO: Explore generating the meta-graph from the SCCs
# - draw the edges
# - verify it is a DAG, i.e. you can toposort it

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
    print(number_of_strongly_connected_components(adj))
