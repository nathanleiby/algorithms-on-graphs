# Week 3

## breadth first search
https://www.coursera.org/learn/algorithms-on-graphs/lecture/bxu5y/breadth-first-search

start a some node
travel outward via ALL edges
nodes can be in one of 3 states: unvisited, processing, done
edges can be in one of 3 states: unvisited, processing, done

as we explore, we label nodes from each sweep with a number (distance)
if nodes are NOT reachable from S, it has distance infinity. So we default to setting distance to all things to infintiy.

Directed vs Undirected... pretty much the same.

To implement, we must do things turn-by-turn ("rounds")

Nodes enter the queue and await their turn to be processed.
When it's in the queue, we also must tag it with the layer it's from
FIFO queue means we process things in distance order.


for all nodes n in graph
    set dist[n] = infinity

dist[start_node] = 0 # distance

add start node to queue and assign distance = d

while nodes in queue:
    pop a node, `n`
    mark n as `visited`
    for each node `m` that `n` has an edge to ...
        if visited (i.e. distance != infinity)
            continue
        else
            add each of these to the queue, and assign them distance `distance = n.distance() + 1`

### Runtime

`O(|E| + |V|)`

At most, we examine edges twice in an undirected graph.

### Proof of Correctness

(I skimmed this b/c late. Intuitively makes sense but I could use more formal practice writing proofs by contradiction.)

## Shortest-path tree

Finding the shortest-path. Same algo as BFS *Except* you need to store previous_nodes 

1. at start, for all nodes set `prev[u] = nil` 
2. when enqueueing new node `v`, record their prev .. `prev[v] = u`

Reconstructing the shorest path from `u`... Start at `u` and find prevs until you get to sought start node `s`



