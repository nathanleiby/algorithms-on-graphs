package main

import (
	"fmt"
	"io/ioutil"

	"github.com/jszwec/csvutil"
)

const dataFile = "../data/san-francisco-california_graph.csv"

// const dataFile = "../data/sample.csv"

// Row ...
type Row struct {
	FromID       int64   `csv:"from_id"`
	ToID         int64   `csv:"to_id"`
	D            float64 `csv:"d"`
	DWeighted    float64 `csv:"d_weighted"`
	Time         float64 `csv:"time"`
	TimeWeighted float64 `csv:"time_weighted"`
}

func readCSV() ([]Row, error) {
	b, err := ioutil.ReadFile(dataFile)
	if err != nil {
		return nil, err
	}
	var rows []Row
	err = csvutil.Unmarshal(b, &rows)
	if err != nil {
		return nil, err
	}

	return rows, nil
}

// run locally via:
// go mod init github.com/nathanleiby/algorithms-on-graphs/week6
// go run github.com/nathanleiby/algorithms-on-graphs/week6

func main() {
	fmt.Println("main")
	rows, err := readCSV()
	if err != nil {
		panic(err)
	}
	fmt.Printf("# Rows = %d\n", len(rows))
	fmt.Printf("%+v\n", rows[0])
	edges := EdgeList{}
	for _, r := range rows {
		edges = append(edges, Edge{
			Source:      Vertex(r.FromID),
			Destination: Vertex(r.ToID),
			Weight:      r.Time,
		})
	}

	fmt.Printf("# Vertices (Edg List)= %d\n", len(edges.Vertices()))
	fmt.Printf("# Edges (Edg List)= %d\n", len(edges.Edges()))

	al := convertEdgeListToAdjacencyList(edges)
	fmt.Printf("# Vertices (Adj List) = %d\n", len(al.Vertices()))
	fmt.Printf("# Edges (Adj List) = %d\n", len(al.Edges()))

	// 1 step path
	// (-122.4067318,37.6552092) => (-122.4066705,37.6554806)
	fmt.Println("")
	p, err := Dijkstra(al, 32927063, 2262036212)
	if err != nil {
		fmt.Println("Dijkstra error: ", err.Error())
	}
	fmt.Println("Path Steps = ", len(p))
	fmt.Println("Path Weight = ", getPathWeight(p))
	fmt.Printf("Path = %+v\n", p)
	fmt.Println("")

	// Unknown path
	// => (-122.3956858,37.6666107)
	// https://www.google.com/maps/place/37%C2%B039'59.8%22N+122%C2%B023'44.5%22W/@37.6897163,-122.4155747,11.42z/data=!4m5!3m4!1s0x0:0x0!8m2!3d37.6666107!4d-122.3956858
	fmt.Println("")

	p, err = Dijkstra(al, 32927063, 1096003072)
	if err != nil {
		fmt.Println("Dijkstra error: ", err.Error())
	}
	fmt.Println("Path Steps = ", len(p))
	fmt.Println("Path Weight = ", getPathWeight(p))
	fmt.Printf("Path = %+v\n", p)
	fmt.Println("")

	// South SF => Oakland
	//          => (-122.2796971,37.8012714)
	// https://www.google.com/maps/place/37%C2%B039'59.8%22N+122%C2%B023'44.5%22W/@37.6897163,-122.4155747,11.42z/data=!4m5!3m4!1s0x0:0x0!8m2!3d37.6666107!4d-122.3956858
	// result...
	// Path Steps =  626
	// Path Weight =  1504.4395644354097

	// Route in Google Maps:
	// https://www.google.com/maps/dir/'37.6552092,-122.4067318'/'37.8012714,-122.2796971'/@37.7412534,-122.4084235,12z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d-122.4067318!2d37.6552092!1m3!2m2!1d-122.2796971!2d37.8012714!3e0
	fmt.Println("")

	p, err = Dijkstra(al, 32927063, 30373973)
	if err != nil {
		fmt.Println("Dijkstra error: ", err.Error())
	}
	fmt.Println("Path Steps = ", len(p))
	fmt.Println("Path Weight = ", getPathWeight(p))
	fmt.Printf("Path = %+v\n", p)
	fmt.Println("")

}

func getPathWeight(p Path) float64 {
	total := float64(0)
	for _, e := range p {
		total += e.Weight
	}
	return total
}
