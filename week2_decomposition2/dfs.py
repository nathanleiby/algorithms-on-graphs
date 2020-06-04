# Uses python3

import sys
import random


class HasCycleException(Exception):
    pass


def dfs(adj):
    """ dfs does a depth-first-search """
    ## TODO: Randomize order that we traverse the nodes,
    ##      to ensure not sensitive to increasing vertex idx
    visited = [False] * len(adj)
    for v in range(len(adj)):
        if visited[v]:
            continue
        explore(adj, visited, v, [v])

    # we should have visited every vertex
    assert all(visited)


def explore(adj, visited, v, ancestors):
    """ explore all vertices that can be reached from v, marking them as visited """
    visited[v] = True
    for neighbor in adj[v]:
        if neighbor in ancestors:
            # error if we find a back-edge, which indicates a cycle in a DAG
            raise HasCycleException(
                "Cycle found where {} has back-edge to {}".format(v, neighbor)
            )
        if not visited[neighbor]:
            explore(adj, visited, neighbor, ancestors + [neighbor])

    # we should have visited all neighbors of this vertex
    assert (neighbor in visited for neighbor in adj[v])


## ALTERNATE IMPLEMENTATION, using pre-post visit
def new_bookkeeping(adj):
    return dict(
        previsit=[0] * len(adj),
        postvisit=[0] * len(adj),
        counter=0,
        # TODO: do i need this in addition to pre/post visit?
        visited=[False] * len(adj),
    )


def dfs2(adj, err_on_cycle=True):
    """ dfs does a depth-first-search """
    bookkeeping = new_bookkeeping(adj)

    v_list = list(range(len(adj)))
    random.shuffle(v_list)  # prove that order doesn't matter
    for v in v_list:
        if not bookkeeping["visited"][v]:
            explore2(adj, v, bookkeeping, err_on_cycle=err_on_cycle)

    # we should have visited every vertex
    assert all(bookkeeping["visited"])
    # we should have written a previsit and postvisit for every vertex
    assert all(map(lambda x: x > 0, bookkeeping["previsit"]))
    assert all(map(lambda x: x > 0, bookkeeping["postvisit"]))
    assert max(bookkeeping["postvisit"]) == bookkeeping["counter"]

    return bookkeeping


def explore2(adj, v, bookkeeping, err_on_cycle=True):
    """ explore all vertices that can be reached from v, marking them as visited """
    previsit(v, bookkeeping)
    bookkeeping["visited"][v] = True
    neighbors = adj[v]
    random.shuffle(neighbors)  # prove that order doesn't matter
    for n in neighbors:
        # error if we find a back-edge, which indicates a cycle in a DAG
        if (
            err_on_cycle
            and bookkeeping["previsit"][n] > 0
            and bookkeeping["postvisit"][n] == 0
        ):
            raise HasCycleException(
                "Cycle found where {} has back-edge to {}".format(v, n)
            )
        if not bookkeeping["visited"][n]:
            explore2(adj, n, bookkeeping, err_on_cycle)

    # we should have visited all neighbors of this vertex
    assert (neighbor in bookkeeping["visited"] for neighbor in adj[v])
    postvisit(v, bookkeeping)


def previsit(v, bookkeeping):
    bookkeeping["counter"] += 1
    bookkeeping["previsit"][v] = bookkeeping["counter"]


def postvisit(v, bookkeeping):
    bookkeeping["counter"] += 1
    bookkeeping["postvisit"][v] = bookkeeping["counter"]
