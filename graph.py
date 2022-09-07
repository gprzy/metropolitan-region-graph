from queue import Queue

class Graph():
    def __init__(self, adjacency_matrix=None):
        if adjacency_matrix:
            self.graph = adjacency_matrix
        else:
            self.graph = {}

    def add_vertex(self, vertex):
        if vertex in self.graph:
            print(f'vértice {vertex} já existe!')
        else:
            self.graph[vertex] = {}

    def add_edge(self, vertex_a, vertex_b, weight):
        if self.has_edge(vertex_a, vertex_b):
            print(f'aresta {(vertex_a, vertex_b)} já existe!')
        else:
            self.graph[vertex_a][vertex_b] = weight
            self.graph[vertex_b][vertex_a] = weight

    def remove_edge(self, vertex_a, vertex_b):
        nova_lista = []
        if self.has_edge(vertex_a, vertex_b):
            for i in self.graph[vertex_a]:
                if i[0] != vertex_b:
                    nova_lista.append(i)
            self.graph[vertex_a] = nova_lista
        else:
            print(f'aresta {(vertex_a, vertex_b)} não existe!')

    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            print(f'vértice {vertex} não existe!')
        else:
            del self.grafo[vertex]

    def has_edge(self, vertice1, vertice2):
        if vertice1 not in self.graph or vertice2 not in self.graph:
            return False
        for i in self.graph[vertice1]:
            if i[0] == vertice2:
                return True
        return False

    def weight(self, vertex_a, vertex_b):
        if self.has_edge(vertex_a, vertex_b):
            return self.graph[vertex_a][vertex_b]
        return f'aresta {(vertex_a, vertex_b)} não existe!'

    def degree(self, vertex):
        if vertex in self.graph:
            return len(self.graph[vertex])
        return f'vértice {vertex} não existe'

    def get_adjacency_matrix(self, pretty=False):
        if pretty:
            for node, neighbors in zip(list(self.graph.keys()),
                                       list(self.graph.values())):
                print(node, neighbors)
        else:
            return self.graph

    def depth_first_search(self, start):
        visited = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack.extend(set(self.graph[vertex].keys()) - set(visited))
        return visited

    def breadth_first_search(self, start):
        visited = [start]
        queue = Queue()
        queue.put(start)
        while not queue.empty():
            vertex = queue.get()
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.put(neighbor)
        return visited

    def dijkstra(self, start='A', end='C'):
        nodes = list(self.graph.keys())
        unvisited = {node: None for node in nodes}
        current_distance = 0
        unvisited[start] = current_distance
        visited = {}

        while end not in visited:
            for neighbour, distance in self.graph[start].items():
                if neighbour not in unvisited:
                    continue

                new_distance = current_distance + distance

                if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
                    unvisited[neighbour] = new_distance

            visited[start] = current_distance
            del unvisited[start]
            
            if not unvisited:
                break
            
            candidates = [node for node in unvisited.items() if node[1]]
            start, current_distance = sorted(candidates, key = lambda x: x[1])[0]

        path = list(visited.keys())
        cost = list(visited.values())[-1]
        return path, cost