# Uses python3

import math
import random
import sys

# relax modifies the distances, if possible
def relax(adj, cost, distance, prev):
    update_occurred = False

    # for each vertex 
    for v in range(len(adj)):
        # relax neighbors
        for idx, neighbor in enumerate(adj[v]):
            c = cost[v][idx]
            relaxed_cost = distance[v] + c 
            if relaxed_cost < distance[neighbor]:
                update_occurred = True
                distance[neighbor] = relaxed_cost
                prev[neighbor] = v

    return update_occurred

def bellman_ford(adj, cost, s):
    # This algo will give us two results:
    # (1) the shortest path from s to every other vertex
    # (2) whether or not the graph has a negative cycle

    # initialize
    distance = []
    prev = []
    for _ in range(len(adj)):
        distance.append(math.inf)
        prev.append(None)
    distance[s] = 0

    # for |vertex|+1 rounds...
    for _ in range(len(adj)-1):
        print(distance)
        did_relax = relax(adj, cost, distance, prev)
        if not did_relax:
            # exit early
            print("exit early")
            return distance, False

    has_negative_cycle = relax(adj, cost, distance, prev)
    return distance, has_negative_cycle
    
# return 1 if graph has negative cycle and 0 if not
def negative_cycle(adj, cost):
    # doesn't matter what starting node we choose, 
    # as long as graph is one connected component
    vertices = list(range(len(adj)))
    start_v = random.choice(vertices)

    _, has_negative_cycle = bellman_ford(adj, cost, start_v)

    return int(has_negative_cycle)

def parse_input(text):
    data = list(map(int, text.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3])
    )
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    return adj, cost

if __name__ == "__main__":
    print(*parse_input(sys.stdin.read()))
