from unorientedGraph import Graph

exampleGraph = {
  "A": ["B", "D"],
  "B": ["A", "C", "E"],
  "C": ["B", "D", "E"],
  "D": ["A", "C", "E"],
  "E": ["B", "C", "D"],
  "F": [],
}

g = Graph()

g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_node("F")

g.add_edge(("A", "B"))
g.add_edge(("A", "D"))
g.add_edge(("B", "C"))
g.add_edge(("B", "E"))
g.add_edge(("C", "D"))
g.add_edge(("C", "E"))
g.add_edge(("E", "D"))

print(g)
