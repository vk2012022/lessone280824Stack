class Graph:
   def __init__(self):
       self.graph = {}

   def add_edge(self, u, v):
       # Добавление ребра в граф
       if u not in self.graph:
           self.graph[u] = []
       self.graph[u].append(v)

   def print_graph(self):
       # Вывод графа в удобочитаемом формате
       for node in self.graph:
           print(node, "->", " -> ".join(map(str, self.graph[node])))

# Пример использования графа с изменёнными данными
g = Graph()

g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

g.print_graph()
