class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        # Добавление вершины в граф
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Добавление ребра между двумя вершинами (неориентированный граф)
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def bfs(self, start):
        # Поиск в ширину (BFS)
        visited = set()
        queue = [start]
        visited.add(start)
        result = []

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return result

    def dfs(self, start, visited=None):
        # Поиск в глубину (DFS)
        if visited is None:
            visited = set()

        visited.add(start)
        result = [start]

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result += self.dfs(neighbor, visited)

        return result


# Пример использования графа:
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

print("Граф:", g.graph)
print("BFS:", g.bfs("A"))
print("DFS:", g.dfs("A"))
