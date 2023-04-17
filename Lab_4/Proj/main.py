import sys


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def searching_algo_BFS(self, s, t, parent):
        visited = [False] * self.ROW
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0
        chosen_paths = []

        while self.searching_algo_BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            chosen_path = []
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                chosen_path.append(s)
                s = parent[s]

            chosen_paths.append(list(reversed(chosen_path + [source])))

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow, chosen_paths

    def read_matrix_from_txt(self):
        with open(self, 'r') as file:
            return [list(map(int, line.strip().split())) for line in file.readlines()[1:]]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input_file")
        sys.exit(1)
    file_path = sys.argv[1]

    graph = Graph.read_matrix_from_txt(file_path)
    g = Graph(graph)

    source = 0
    sink = len(graph) - 1

    max_flow, chosen_paths = g.ford_fulkerson(source, sink)

    print("Max Flow: %d " % max_flow)
    print("Paths: ", chosen_paths)
