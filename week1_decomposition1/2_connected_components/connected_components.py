#Uses python3

import sys


def number_of_components(adj):
    result = 0
    #print(adj)
    visited = {}
    for idx in range(len(adj)):
        if idx in visited:
            continue

        # dfs another connected component
        # print("DFS idx=", idx)
        result += 1
        vertices = get_vertices_in_component_containing_x(adj, idx)
        for v_idx in vertices:
            visited[v_idx] = True

    return result

def get_vertices_in_component_containing_x(adj, x):
    # do depth first search starting from vertex x
    visited = {}
    to_visit = [x]
    while len(to_visit) > 0:
        # my guess is that this loop is quite slow for graphs with tons of edges
        # .. it's doing an array pop() and an array filter() on large arrays (O(1M) items) 
        cur = to_visit.pop() 
        visited[cur] = True
        neighbors = adj[cur]
        unvisited_neighbors = filter(lambda x: x not in visited, neighbors)
        to_visit.extend(unvisited_neighbors)

    # return every visited node
    return visited.keys()

def parse_input(text):
    data = list(map(int, text.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return adj

if __name__ == '__main__':
    adj = parse_input(sys.stdin.read())
    print(number_of_components(adj))
