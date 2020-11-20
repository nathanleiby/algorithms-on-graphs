# week 6

- We've learned classical shortest path algos.
- Advanced algos can be faster (1000x or 1Mx), but the work for particular kinds of graphs. For example: road networks, social networks.
- These are optimizations based on Djikstra's Algorithm


## Djikstra's (Review)

Nate reviewing + reading wiki

```
djikstra(graph, src, dest):
    # initialize record keeping
    unvisited = set()
    distance = {}
    for node in graph:
        unvisited.add(node)
        distance[node] = infinity

    # starting node
    distance[src] = 0
    cur_node = src

    # explore the graph
    while len(unvisited) > 0:
        # get next node: with minimum distance
        min_node = None
        for n in unvisited:
            if n.weight < math.inf:
                if min_node:
                    if n.weight  < min_node.weight:
                        min_node = n
                else:
                    min_node = n
        if not min_unvisited:
            fail to find

        visited.add(cur_node)
        for e in edges(cur_node):
            if e.dest in unvisited:
                # update distance, if shorter one found
                distance[e.dest] = min(distance[e.dest], distance[e.src] + e.weight)
                # todo: can track previous, too

```

### Bidirectional Search

MUST have non-negative edge weights. This is true for all graphs in this section.
