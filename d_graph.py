# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Adds a vertex to the graph
        :return: Total number of vertices after addition
        """
        if self.v_count == 0:
            self.adj_matrix = [[0]]
            self.v_count += 1
            self.adj_matrix[0][0] = 0
            return 1
        self.adj_matrix.append([0 for _ in range(self.v_count)])
        self.v_count += 1
        for i in range(self.v_count):
            self.adj_matrix[i].append(0)
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds an edge to current graph
        :param src: Vertex 1
        :param dst: Vertex 2
        :param weight: weight of path between the two vertex
        :return: None
        """
        if src > (len(self.adj_matrix) - 1) or dst > (len(self.adj_matrix[0]) - 1):
            return
        if weight < 0:
            return
        if src is dst:
            return
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge between vertex
        :param src: vertex 1
        :param dst: vertex 2
        :return: None
        """
        if src > (len(self.adj_matrix) - 1) or dst > (len(self.adj_matrix[0]) - 1):
            return
        if src < 0 or dst < 0:
            return
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Gets all vertices in current graph
        :return: list of vertices
        """
        list = []
        for i in range(len(self.adj_matrix)):
            list.append(i)
        return list

    def get_edges(self) -> []:
        """
        Gets all edges in graph
        :return: returns list of edges in current graph
        """
        list = []
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] > 0:
                    list.append((i, j, self.adj_matrix[i][j]))
        return list

    def is_valid_path(self, path: []) -> bool:
        """
        Checks if a path is valid in graph
        :param path: Path to check
        :return: Boolean if path is valid
        """
        for i in range(len(path) - 1):
            if self.adj_matrix[path[i]][path[i + 1]] > 0:
                continue
            else:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Performs depth first search on map
        :param v_start: Starting vertex
        :param v_end: Ending Vertex
        :return: List of traversal order
        """
        if v_start not in self.get_vertices():
            return []
        visited = self.rec_dfs(v_start, visited=[])
        for i in range(len(visited)):
            if visited[i] is v_end:
                visited = visited[:i + 1]
                break
        return visited

    def rec_dfs(self, current, visited):
        """
        Recursive dfs function
        :param current: Current vertex
        :param visited: List of visited vertices
        :return: List of order of traversal
        """
        if current not in visited:
            visited.append(current)
            adjacent = []
            for i in range(len(self.adj_matrix[current])):
                if self.adj_matrix[current][i] > 0:
                    adjacent.append(i)
            for _ in adjacent:
                self.rec_dfs(_, visited)
        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        Performs breadth first search on map
        :param v_start: Starting vertex
        :param v_end: Ending Vertex
        :return: List of traversal order
        """
        if v_start not in self.get_vertices():
            return []
        visited = self.rec_bfs(v_start, visited = [], queue = [])
        for i in range(len(visited)):
            if visited[i] is v_end:
                visited = visited[:i + 1]
                break
        return visited

    def rec_bfs(self, current, visited, queue):
        """
        Recursive bfs function
        :param current: Current vertex
        :param visited: List of visited vertices
        :param queue: queue of next exploration
        :return: List of order of traversal
        """
        visited.append(current)
        queue.append(current)
        while queue:
            temp = queue.pop(0)
            adjacent = []
            for i in range(len(self.adj_matrix[temp])):
                if self.adj_matrix[temp][i] > 0:
                    adjacent.append(i)
            adjacent.sort()
            for _ in adjacent:
                if _ not in visited:
                    visited.append(_)
                    queue.append(_)
        return visited

    def has_cycle(self):
        """
        Checks if graph has a cycle
        :return: Boolean on whether cycle exits
        """
        cycle = False
        color = {}
        for i in self.get_vertices():
            color[i] = 'W'
        for i in self.get_vertices():
            if color[i] is 'W':
                cycle = self._has_cycle(i, color)
                if cycle:
                    break
        return cycle

    def _has_cycle(self, i, color):
        """
        Recursive cycle function
        :param i: Current vertex
        :param color: Color shading method
        :return: Boolean result of check
        """
        color[i] = 'G'
        adjacent = []
        for k in range(len(self.adj_matrix[i])):
            if self.adj_matrix[i][k] > 0:
                adjacent.append(k)
        for j in adjacent:
            if color[j] is 'W':
                cycle = self._has_cycle(j, color)
                if cycle:
                    return True
            elif color[j] is 'G':
                return True
        color[i] = 'B'
        return False

    def dijkstra(self, src: int) -> []:
        """
        Performs Dijkstra's low cost algorithm to find the lowest traversal cost from on vertex to another
        :param src: Starting vertex
        :return: list of total costs
        """
        visited = [None for i in range(len(self.adj_matrix))]
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, src))
        while heap:
            v = heapq.heappop(heap)
            d = v[0]
            v = v[1]
            if visited[v] is None:
                visited[v] = d
                for i in range(len(self.adj_matrix[v])):
                    if self.adj_matrix[v][i] > 0:
                        d_i = self.adj_matrix[v][i]
                        d_i = d_i + d
                        heapq.heappush(heap, (d_i, i))
                        heap.sort()
        for i in range(len(visited)):
            if visited[i] is None:
                visited[i] = float("inf")
        return visited

if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
