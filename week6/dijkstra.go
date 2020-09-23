package main

import (
	"fmt"
	"math"
)

// DistanceEstimates tracks the distance estimates while running Dijkstra's
type DistanceEstimates map[Vertex]float64

// Previous tracks the previous vertex in the Path
type Previous map[Vertex]*Vertex

// Visited tracks visited vertices
type Visited map[Vertex]bool

// Dijkstra runs Dijkstra's algorithm on a graph
func Dijkstra(g GraphIface, src, dst Vertex) (Path, error) {
	// Create a 'visited' map to track visited vertices. initialize to empty map.
	visited := Visited{}

	// Create a 'distance' map. initialize all vertices with value of infinity
	vertices := g.Vertices()
	distance := DistanceEstimates{}
	previous := Previous{}
	for _, v := range vertices {
		distance[v] = math.Inf(1)
		previous[v] = nil
	}
	// Set distance to src to = 0
	distance[src] = 0

	// While some vertices are unvisited and we haven't added dst to visited yet
	for i := 0; i < len(vertices); i++ {
		//	pick the vertex in 'distance' with the minimum value
		minVertex := getMinVertex(distance, visited)
		//  relax its edges
		relax(minVertex, g, distance, previous)

		//  add vertex to visited
		visited[minVertex] = true

		if visited[dst] {
			// we can short-circuit if just looking for a path
			break
		}
	}

	return constructPath(g, previous, src, dst)
}

// TODO: use a heap or pQueue
// https://golang.org/pkg/container/heap/
func getMinVertex(distance DistanceEstimates, visited Visited) Vertex {
	minValue := math.Inf(1)
	var minVertex Vertex
	for vertex, value := range distance {
		if value < minValue && !visited[vertex] {
			minVertex = vertex
			minValue = value
		}
	}
	return minVertex
}

func relax(v Vertex, g GraphIface, distance DistanceEstimates, previous Previous) {
	// get neighbors for vertex
	edges := getEdgesForVertex(v, g)
	for _, e := range edges {
		// if we can improve the estimate, do so
		distanceViaV := distance[v] + e.Weight
		if distanceViaV < distance[e.Destination] {
			distance[e.Destination] = distanceViaV
			previous[e.Destination] = &v
		}
	}
}

func getEdgesForVertex(v Vertex, g GraphIface) []Edge {
	edges := []Edge{}
	for _, e := range g.Edges() {
		if e.Source == v {
			edges = append(edges, e)
		}
	}
	return edges
}

func constructPath(g GraphIface, previous Previous, src Vertex, dst Vertex) (Path, error) {
	// Create path
	if previous[dst] == nil {
		return Path{}, fmt.Errorf("no path found")
	}

	cur := dst
	path := Path{}
	edges := g.Edges()
	for cur != src {
		prev := previous[cur]
		found := false
		for _, e := range edges {
			if e.Source == *prev && e.Destination == cur {
				path = append(path, e)
				cur = *prev
				found = true
				break
			}
		}
		if !found {
			panic("invalid edge")
		}
	}
	// reverse
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}

	return path, nil
}
