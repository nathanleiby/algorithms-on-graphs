# Uses python3

import sys
import queue
import math


def distance(adj, s, t):
    # print("distance(", adj, s, t, ")")
    print("")
    print("distance()")
    print("ADJ:")
    for l in adj:
        print(l)
    print("")
    print("Find distance from s={} to t={}".format(s, t))

    # initialize distance and prev nodes
    dist = {}
    prev = {}
    for v in range(len(adj)):
        dist[v] = math.inf
        prev[v] = None

    # enqueue the start node
    dist[s] = 0
    q = queue.Queue()
    q.put(s)

    # start BFS-ing
    while not q.empty():
        cur = q.get()
        for n in adj[cur]:
            if dist[n] < math.inf:
                # already visited
                continue
            dist[n] = dist[cur] + 1
            prev[n] = cur

            # is it the one we're looking for?
            if n == t:
                return dist[n]

            q.put(n)

    return -1


def parse_input(text):
    data = list(map(int, text.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    return adj, s, t


if __name__ == "__main__":
    text = sys.stdin.read()
    adj, s, t = parse_input(text)
    print(distance(adj, s, t))
