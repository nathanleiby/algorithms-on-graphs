# Uses python3

import sys
import logging
import math

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
# logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def distance(adj, cost, s, t):
    # initialize all distances to inf
    distance = []
    for _ in range(len(adj)):
        distance.append(math.inf)

    # keep track of nodes we've explored.
    known_region = set()

    # initialize algo
    known_region.add(s)
    current = s
    distance[s] = 0

    # while known region doesn't include all nodes/vertices
    while len(known_region) < len(adj):
        logging.debug(
            "Current vertex: {} (dist = {})".format(current, distance[current])
        )

        # visit all of current vertex's neighbors
        for idx, neighbor in enumerate(adj[current]):
            c = cost[current][idx]
            logging.debug("\t{} => {} ... cost = {}".format(current, neighbor, c))

            # update distances, if better path found ("relax")
            distance_via_current = distance[current] + c
            if distance_via_current < distance[neighbor]:
                distance[neighbor] = distance_via_current

        # add current to known_region
        known_region.add(current)

        # find the unexplored node with the minimum distance and set it to current
        # "extract_min"...
        # TODO: consider optimizing perf via priority queue https://docs.python.org/3/library/heapq.html
        logging.debug("Distances after update:")
        logging.debug(distance)

        min_vertex = None
        min_distance = math.inf
        for v, dist in enumerate(distance):
            if (v not in known_region) and (dist <= min_distance):
                min_vertex = v
                min_distance = dist
        current = min_vertex

    if distance[t] == math.inf:
        return -1
    else:
        return distance[t]


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
    s, t = data[0] - 1, data[1] - 1

    logging.debug(adj)
    logging.debug(cost)
    logging.debug("")

    return adj, cost, s, t


if __name__ == "__main__":
    text = sys.stdin.read()
    adj, cost, s, t = parse_input(text)
    print(distance(adj, cost, s, t))
