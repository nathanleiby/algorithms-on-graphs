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
// TODO: Could refactor to `type Vertex int64` to remove lots of unnecessay complexity in my code
type Vertex struct {
	ID int64
}

func (v Vertex) String() string {
	return fmt.Sprintf("%d", v.ID)
}

// GraphIface is the interface for a graph
type GraphIface interface {
	Vertices() []Vertex
	Edges() []Edge
}

// EdgeList is a Graph represented as a list of edges
// TODO: Explore other Graph representations
type EdgeList []Edge

// Edges gives the edges in the graphs
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
