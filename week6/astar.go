package main

// Dijstra's
// 1. Initialize distances (infinity for all vertices)
// 2. Set distance to start vertex to 0
// 3. Visited = empty set
// Loop:
//   - Choose vertex v with minimum distance # from a heap/pqueue
//   - Relax edges (update distances on all connected vertexes)
//	 - Mark v as explored

// AStar ...
// AStar runs AStar algorithm on a graph
func AStar(g GraphIface, src, dst Vertex) (Path, error) {
	// ASTAR is
	// 1. Initialize distances (infinity for all vertices)
	// 2. Set distance to start vertex to 0
	// *NEW* Initialize potentials (e.g. in road scenario, potential could be the straight line distance from each vertex to the destination vertex)
	// 3. Visited = empty set
	// Loop:
	//   - *UPDATED* Choose vertex v with minimum distance + potential # from a heap/pqueue
	//   - Relax edges (update distances on all connected vertexes)
	//	 - Mark v as explored
	return Path{}, nil
}

// BidirectionalAStar ...
func BidirectionalAStar() {
	// Do Astar on Graph and reverse Graph
	// should stop
}
