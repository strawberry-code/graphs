from unorientedGraph import Graph

exampleGraph = {
  "A": ["B", "D"],
  "B": ["A", "C", "E"],
  "C": ["B", "D", "E"],
  "D": ["A", "C", "E"],
  "E": ["B", "C", "D"],
  "F": [],
}

g = Graph(exampleGraph)
print(g)
