# Uses python3

import sys


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
def dfs2(adj):
    """ dfs does a depth-first-search """
    bookkeeping = dict(
        previsit=[0] * len(adj),
        postvisit=[0]*len(adj),
        counter=0,

        # TODO: do i need this in addition to pre/post visit?
        visited=[False] * len(adj),
    )
    # TODO: randomize
    # for v in random.shuffle(range(len(adj))):
    for v in range(len(adj)):
        if bookkeeping['visited'][v]:
            continue
        explore2(adj, v, bookkeeping)

    # we should have visited every vertex
    assert all(bookkeeping['visited'])
    # we should have written a previsit and postvisit for every vertex
    assert all(map(lambda x: x > 0, bookkeeping['previsit']))
    assert all(map(lambda x: x > 0, bookkeeping['postvisit']))
    assert max(bookkeeping['postvisit']) == bookkeeping['counter']

    return bookkeeping

def explore2(adj, v, bookkeeping):
    """ explore all vertices that can be reached from v, marking them as visited """
    previsit(v, bookkeeping)
    bookkeeping['visited'][v] = True
    for neighbor in adj[v]:
        # error if we find a back-edge, which indicates a cycle in a DAG
        if bookkeeping['previsit'][neighbor] > 0 and bookkeeping['postvisit'][neighbor] == 0:
            raise HasCycleException(
                "Cycle found where {} has back-edge to {}".format(v, neighbor)
            )
        if not bookkeeping['visited'][neighbor]:
            explore2(adj, neighbor, bookkeeping)

    # we should have visited all neighbors of this vertex
    assert (neighbor in bookkeeping['visited'] for neighbor in adj[v])
    postvisit(v, bookkeeping)


def previsit(v, bookkeeping):
    bookkeeping['counter'] += 1
    bookkeeping['previsit'][v] = bookkeeping['counter']

def postvisit(v, bookkeeping):
    bookkeeping['counter'] += 1
    bookkeeping['postvisit'][v] = bookkeeping['counter']