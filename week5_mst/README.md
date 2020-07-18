# week 5 lecture notes: minimum spanning trees (MST)

## Cut property (Lemma)

Assume we have a set of edges `X` that is a subset of the edges `E` of some MST on graph `G(V, E)`.

Now, let us device the vertices of the graph into `S` and `V - S`, such that no edge in `X` cross between these two groups.

There's some other edge `e \in E` that is the lightest edge across this partition.

=> `X + {e}` is also a part of some MST.

Proof (in words):
Suppose that `e` isn't part of the MST, and instead some other edge `e'` crossing between the groups is required. Because that edge has a heigher weight than `e`, if we replaced `e'` with `e` then the tree would still be connected AND it would have a lower weight. Thus the previous tree couldn't have been the _minimum_ spanning tree.

## Kruskal's algorithm

Think in terms of edges...

```
Let `X` be the set of edges in our output MST.
Let `R` be the set of remaining edges to explore.
While some vertices aren't connected (i.e. `|X| < |E| - 1`)
    Find shortest edge `e` in `R`
    If adding `e` to `X` would create cycle
        Remove `e` from `R`
    Else
        X = X + {e}
```

## Prim's algorithm
Think in terms of vertices

```
Exists a graph G(V,E).
Let `E_mst` be the set of edges in our output MST.
Let `V_explored` be the set of explored vertices.
Pick a starting vertex `v`.
While some vertices aren't connected (i.e. `|X| < |E| - 1`)
    From `v` explore all its edges
    Find the edge `e` to an unexplored vertex with the lowest weight and add it to `E_mst`
    Add `v` to `V_explored`
    Update `v` to be the destination of the edge `e`
```
