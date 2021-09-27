# Course: Computer Science 261
# Author: Benjamin Warren
# Assignment: Assignment 6 - Graphs
# Description: Implementing an undirected graph

class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Adds a vertex to graph
        :param v: Vertex to add
        :return:None
        """
        if v in self.adj_list:
            return
        else:
            self.adj_list[v] = []
        
    def add_edge(self, u: str, v: str) -> None:
        """
        Adds an edge between vertex
        :param u: vertex 1
        :param v: vertex 2
        :return: None
        """
        if u is v:
            return
        if v not in self.adj_list:
            self.add_vertex(v)
        if u not in self.adj_list:
            self.add_vertex(u)
        if v in self.adj_list[u] or u in self.adj_list[v]:
            return
        self.adj_list[v] += u
        self.adj_list[u] += v

    def remove_edge(self, v: str, u: str) -> None:
        """
        Removes an edge between vertex
        :param v: vertex 1
        :param u: vertex 2
        :return: None
        """
        if u not in self.adj_list or v not in self.adj_list:
            return
        if u in self.adj_list[v] and v in self.adj_list[u]:
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)

    def remove_vertex(self, v: str) -> None:
        """
        Removes vertex from graph
        :param v: Vertex to remove
        :return: None
        """
        if v in self.adj_list:
            for key in self.adj_list:
                self.remove_edge(key, v)
            self.adj_list.pop(v)
        return

    def get_vertices(self) -> []:
        """
        Gets all vertices in current graph
        :return: list of vertices
        """
        list = []
        for key in self.adj_list:
            list.append(key)
        return list

    def get_edges(self) -> []:
        """
        Gets all edges in graph
        :return: returns list of edges in current graph
        """
        copyDict = UndirectedGraph()
        for key in self.adj_list:
            for value in self.adj_list[key]:
                copyDict.add_edge(key, value)
        list = []
        for key in copyDict.adj_list:
            for value in self.adj_list[key]:
                if value in copyDict.adj_list[key]:
                    list.append((key, value))
                    copyDict.remove_edge(key, value)
        return list

    def is_valid_path(self, path: []) -> bool:
        """
        CHecks if a path is valid in graph
        :param path: Path to check
        :return: Boolean if path is valid
        """
        if len(path) > 1:
            i = 0
            edges = self.get_edges()
            while True:
                if path[i] in self.adj_list or path[i + 1] in self.adj_list:
                    if (path[i], path[i + 1]) in edges or (path[i + 1], path[i]) in edges:
                        i += 1
                        try:
                            path[i+1]
                        except IndexError:
                            break
                    else:
                        return False
                else:
                    return False
            return True
        elif len(path) == 1:
            if path[0] in self.adj_list:
                return True
            else:
                return False
        else:
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
        visited = self.rec_dfs(v_start, visited = [])
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
            adjacent = self.adj_list[current]
            adjacent.sort()
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
        :return: List of order of traversal
        """
        visited.append(current)
        queue.append(current)
        while queue:
            temp = queue.pop(0)
            adjacent = self.adj_list[temp]
            adjacent.sort()
            for _ in adjacent:
                if _ not in visited:
                    visited.append(_)
                    queue.append(_)
        return visited

    def count_connected_components(self):
        """
        Counts number of connected components in graph
        :return: Int of separate components
        """
        count = 0
        vertices = self.get_vertices()
        vertices.sort()
        temp = self.dfs(str(vertices[0]))
        temp.sort()
        dfs = [temp]
        count += 1
        for _ in range(len(vertices)):
            temp = self.dfs(str(vertices[_]))
            temp.sort()
            if temp not in dfs:
                count += 1
                dfs = [temp] + dfs
        return count

    def has_cycle(self):
        """
        Checks if graph has a cycle
        :return: Boolean on whether cycle exits
        """
        cycle = False
        color = {}
        parent = {}
        for i in self.adj_list:
            color[i] = 'W'
            parent[i] = None
        for i in self.adj_list:
            if color[i] is 'W':
                cycle = self._has_cycle(i, color, parent)
                if cycle:
                    break
        return cycle

    def _has_cycle(self, i, color, parent):
        """
        Recursive cycle function
        :param i: current vertex
        :param color: displays list of visited vertices based on shading
        :param parent: parent vertex explored
        :return: Boolean result of check
        """
        color[i] = 'G'
        for j in self.adj_list[i]:
            if color[j] is 'W':
                parent[j] = i
                cycle = self._has_cycle(j, color, parent)
                if cycle is True:
                    return True
            elif color[j] is 'G' and parent[i] != j:
                return True
        color[i] = 'B'
        return False

if __name__ == '__main__':
    #
    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = UndirectedGraph()
    # print(g)
    #
    # for v in 'ABCDE':
    #     g.add_vertex(v)
    # print(g)
    #
    # g.add_vertex('A')
    # print(g)
    #
    # for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
    #     g.add_edge(u, v)
    # print(g)
    #
    #
    # print("\nPDF - method remove_edge() / remove_vertex example 1")
    # print("----------------------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # g.remove_vertex('DOES NOT EXIST')
    # g.remove_edge('A', 'B')
    # g.remove_edge('X', 'B')
    # print(g)
    # g.remove_vertex('D')
    # print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    # print("\nPDF - method count_connected_components() example 1")
    # print("---------------------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print(g.count_connected_components(), end=' ')
    # print()
    #
    #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
    #     'add FG', 'remove GE')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print('{:<10}'.format(case), g.has_cycle())
