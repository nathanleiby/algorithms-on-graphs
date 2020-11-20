# TODO

- week5:
  - [ ] PQueue for performance
- [...] week6: watch lectures
- week6: Problem: Compute Distance Faster Using Coordinates

  - [x] watch lectures
  - [x] read up on this and wrote pseudocode
  - [x] prep a dataset (e.g. openstreet map)
    - choose a dataset
    - format it into a graph with LAT/LNG ... edges .. weights .. edge labels
      - use lib to compute dis from LAT/LNG .. straight line faster than great circle (tunnel through earth)
  - [ ] Run my existing code on the dataset
    - [ ] Read in the SF dataset
    - [ ] Build a graph from it
  - [ ] performance -- I think m ygraph repr is likely hella slow because it's not an adjacency list
  - [ ] dream: visualize our computed route
    - [ ] (MVP) visualize the path manually by plotting GPS coordinates as a Google Maps route
  - [ ] Implement AStar
  - [ ] Implement Bidirectional Dijkstra "meet in the middle" logic. Make sure I understand the stopping condition!
    - I think: once you've met in the middle, you now need to check anything in the "open" set to see if there's a path _directly_ from a vertex in the forwards search to one in the backwards search that overall has a length shorter than your best path. If such a path exists, it's the optimal path. Otherwise, your meet in the middle path is optimal.

- Chat about `decomposition2.pdf`: 5.2 "Designing an algo" .. thinking about runtime vs computer speed

---

# 2020-10-25

- PROBLEM:

  - "Find the path from row #1 to row #100"
    - row #1: 37.6552092, -122.4067318 ... The East Side, South San Francisco, California 94080
    - row #100: 37.801271, -122.279697 ... John B. Williams Fwy, Oakland, CA 94607
    - Google maps path (21miles, 21minutes): https://www.google.com/maps/dir/37.6552092,-122.4067318/37.8012714,+-122.2796971/@37.7413828,-122.4085981,12z/data=!4m7!4m6!1m0!1m3!2m2!1d-122.2796971!2d37.8012714!3e0

- Discuss bidirectional dijkstra edge case: https://cs.stackexchange.com/a/57218
