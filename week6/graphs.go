package main

import "fmt"

// Path is a series of edges
type Path []Edge

// Edge is a connection between two vertices
type Edge struct {
	Source      Vertex
	Destination Vertex
	Weight      float64
}

func (e Edge) String() string {
	return fmt.Sprintf("%s->%s (w=%f)", e.Source, e.Destination, e.Weight)
}

// Vertex is a node in the graph
type Vertex int64

func (v Vertex) String() string {
	return fmt.Sprintf("%d", v)
}

// GraphIface is the interface for a graph
type GraphIface interface {
	Vertices() []Vertex
	Edges() []Edge
	GetNeighbors(v Vertex) []Edge
	// Potentials gives results for a "potential" function, e.g. straight line distance from vertex to all other vertexes
	// Potentials(Vertex) map[Vertex]float64
}

// EdgeList is a Graph represented as a list of edges
type EdgeList []Edge

// Edges gives the edges in the graph
func (el EdgeList) Edges() []Edge {
	return el
}

// Vertices gives the vertices in the graph
func (el EdgeList) Vertices() []Vertex {
	vSet := map[Vertex]struct{}{}
	for _, e := range el {
		vSet[e.Destination] = struct{}{}
		vSet[e.Source] = struct{}{}
	}

	vertices := []Vertex{}
	for vertex := range vSet {
		vertices = append(vertices, vertex)
	}
	return vertices
}

// GetNeighbors ...
func (el EdgeList) GetNeighbors(v Vertex) []Edge {
	edges := []Edge{}
	for _, e := range el.Edges() {
		if e.Source == v {
			edges = append(edges, e)
		}
	}
	return edges
}

// TODO: Let's do this later
// // Potentials in EdgeList has no meaning, so we return 0 in all cases
// func (el EdgeList) Potentials() map[Vertex]float64 {
// 	out := map[Vertex]float64{}
// 	for _, v := range el.Vertices() {
// 		out[v] = 0
// 	}
// 	return out
// }

// AdjacencyList is a Graph representation that gives the list of edges for each vertex
type AdjacencyList map[Vertex][]Edge

// Edges gives the edges in the graph
func (al AdjacencyList) Edges() []Edge {
	out := []Edge{}
	for _, edges := range al {
		out = append(out, edges...)
	}
	return out
}

// Vertices gives the vertices in the graph
func (al AdjacencyList) Vertices() []Vertex {
	out := []Vertex{}
	for v := range al {
		out = append(out, v)
	}
	return out
}

// GetNeighbors ...
func (al AdjacencyList) GetNeighbors(v Vertex) []Edge {
	return al[v]
}

func convertEdgeListToAdjacencyList(el EdgeList) AdjacencyList {
	out := map[Vertex][]Edge{}
	for _, edge := range el {
		_, ok := out[edge.Source]
		if !ok {
			// Initialize
			out[edge.Source] = []Edge{}
		}
		_, ok = out[edge.Destination]
		if !ok {
			// initialize
			out[edge.Destination] = []Edge{}
		}

		out[edge.Source] = append(out[edge.Source], edge)
	}
	return out
}
