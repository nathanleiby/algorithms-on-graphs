package main

// // BidirectionalDijkstra runs said algorithm on a graph
// func BidirectionalDijkstra(g GraphIface, src, dst Vertex) (Path, error) {
// 	// Create a 'visited' map to track visited vertices. initialize to empty map.
// 	visited := Visited{}

// 	// Create a 'distance' map. initialize all vertices with value of infinity. Also create a PQ for optimized lookup
// 	// Create a 'previous' map so we can reconstruct the shortest path
// 	previous := Previous{}
// 	distance := Distance{}
// 	pq := NewPriorityQueue()
// 	for _, v := range g.Vertices() {
// 		pq.Insert(v, math.Inf(1))
// 		updateDistance(v, math.Inf(1), pq, distance)
// 		previous[v] = nil
// 	}

// 	// Set distance to src to 0
// 	updateDistance(src, 0, pq, distance)

// 	// While some vertices are unvisited and we haven't added dst to visited yet
// 	for pq.Len() > 0 {
// 		//	get the unvistied vertex with minimum distance estimate
// 		minVertex := getMinVertex(pq)
// 		if visited[minVertex] {
// 			continue
// 		}

// 		//  relax its edges
// 		relax(minVertex, g, pq, distance, previous)

// 		//  add vertex to visited
// 		visited[minVertex] = true

// 		if visited[dst] {
// 			// we can short-circuit if just looking for a path
// 			break
// 		}
// 	}

// 	return constructPath(g, previous, src, dst)
// }

// func getMinVertex(pq PriorityQueue) Vertex {
// 	v, err := pq.Pop()
// 	if err != nil {
// 		panic(err)
// 	}
// 	return v.(Vertex)
// }

// func relax(v Vertex, g GraphIface, pq PriorityQueue, distance Distance, previous Previous) {
// 	// get neighbors for vertex
// 	edges := getEdgesForVertex(v, g)
// 	for _, e := range edges {
// 		// if we can improve the estimate, do so
// 		curDistance := distance[e.Destination]
// 		distanceViaV := distance[v] + e.Weight
// 		if distanceViaV < curDistance {
// 			updateDistance(e.Destination, distanceViaV, pq, distance)
// 			previous[e.Destination] = &v
// 		}
// 	}
// }

// func updateDistance(v Vertex, value float64, pq PriorityQueue, distance Distance) {
// 	pq.UpdatePriority(v, value)
// 	distance[v] = value
// }

// func getEdgesForVertex(v Vertex, g GraphIface) []Edge {
// 	edges := []Edge{}
// 	for _, e := range g.Edges() {
// 		if e.Source == v {
// 			edges = append(edges, e)
// 		}
// 	}
// 	return edges
// }

// func constructPath(g GraphIface, previous Previous, src Vertex, dst Vertex) (Path, error) {
// 	// Create path
// 	if previous[dst] == nil {
// 		return Path{}, fmt.Errorf("no path found")
// 	}

// 	cur := dst
// 	path := Path{}
// 	edges := g.Edges()
// 	for cur != src {
// 		prev := previous[cur]
// 		found := false
// 		for _, e := range edges {
// 			if e.Source == *prev && e.Destination == cur {
// 				path = append(path, e)
// 				cur = *prev
// 				found = true
// 				break
// 			}
// 		}
// 		if !found {
// 			panic("invalid edge")
// 		}
// 	}
// 	// reverse
// 	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
// 		path[i], path[j] = path[j], path[i]
// 	}

// 	return path, nil
// }
