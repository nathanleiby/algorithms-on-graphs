package main

import (
	"reflect"
	"testing"
)

func TestDijkstra(t *testing.T) {
	type args struct {
		g   GraphIface
		src Vertex
		dst Vertex
	}
	maxV := 10
	v := make([]Vertex, maxV)
	for i := 0; i < maxV; i++ {
		v[i] = Vertex(i)
	}

	trivialGraph := EdgeList{
		Edge{v[0], v[1], 1},
	}

	smallGraph := EdgeList{
		Edge{v[0], v[1], 1},
		Edge{v[1], v[2], 1},
		Edge{v[2], v[3], 1},
		Edge{v[0], v[3], 100},
		Edge{v[4], v[0], 1},
	}

	tests := []struct {
		name    string
		args    args
		want    Path
		wantErr bool
	}{
		{
			name: "trivial path",
			args: args{
				g:   trivialGraph,
				src: v[0],
				dst: v[1],
			},
			want:    Path{trivialGraph[0]},
			wantErr: false,
		},
		{
			name: "trivial path (adj list graph)",
			args: args{
				g:   convertEdgeListToAdjacencyList(trivialGraph),
				src: v[0],
				dst: v[1],
			},
			want:    Path{trivialGraph[0]},
			wantErr: false,
		},
		{
			name: "small path",
			args: args{
				g:   smallGraph,
				src: v[0],
				dst: v[3],
			},
			want:    Path{smallGraph[0], smallGraph[1], smallGraph[2]},
			wantErr: false,
		},
		{
			name: "small path (adj list graph)",
			args: args{
				g:   convertEdgeListToAdjacencyList(smallGraph),
				src: v[0],
				dst: v[3],
			},
			want:    Path{smallGraph[0], smallGraph[1], smallGraph[2]},
			wantErr: false,
		},
		{
			name: "no path",
			args: args{
				g:   smallGraph,
				src: v[0],
				dst: v[4],
			},
			want:    Path{},
			wantErr: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := Dijkstra(tt.args.g, tt.args.src, tt.args.dst)
			if (err != nil) != tt.wantErr {
				t.Errorf("Dijkstra() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Dijkstra() = %v, want %v", got, tt.want)
			}
		})
		// algo := "AStar"
		// t.Run(tt.name + " [AStar]", func(t *testing.T) {
		// 	got, err := AStar(tt.args.g, tt.args.src, tt.args.dst)
		// 	if (err != nil) != tt.wantErr {
		// 		t.Errorf("%s() error = %v, wantErr %v", algo, err, tt.wantErr)
		// 		return
		// 	}
		// 	if !reflect.DeepEqual(got, tt.want) {
		// 		t.Errorf("%s() = %v, want %v", algo, got, tt.want)
		// 	}
		// })
	}
}
