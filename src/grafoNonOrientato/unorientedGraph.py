class Graph(object):
    def __init__(self, graph=None):
        if graph is None:
            graph = {}
        self.__graph = graph

    def add_node(self, node):
        if node not in self.__graph:
            self.__graph[node] = []

    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.__graph:
            self.__graph[node1].append(node2)
        else:
            self.__graph[node1] = [node2]

    def nodes(self):
        return list(self.__graph.keys())

    def edges(self):
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                if (neighbour, node) not in edges:
                    edges.append((node, neighbour))
        return edges

    def __str__(self):
        res = "nodes: "
        for node in self.nodes():
            res += str(node) + " "
        res += "\nedges: "
        for edge in self.edges():
            res += str(edge) + " "
        res += "\nisolated nodes: "
        for node in self.nodes():
            if len(self.__graph[node]) == 0:
                isIsolated = True
                for n in self.nodes():
                    if node != n:
                        if node in self.__graph[n]:
                            isIsolated = False
                if isIsolated:
                    res += str(node) + " "
        return res
