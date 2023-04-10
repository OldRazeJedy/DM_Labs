import sys
import random


with open(sys.argv[1], 'r') as file:
    n = int(file.readline())
    graph = []
    for i in range(n):
        row = list(map(int, file.readline().split()))
        graph.append(row)

for i in range(n):
    degree = sum(1 for j in range(n) if graph[i][j] > 0)
    if degree < n / 2:
        print("Hamiltonian cycle does not exist")
        sys.exit()

start = 0
path = [start]
visited = [False] * n
visited[start] = True

while len(path) < n:
    current = path[-1]
    min_distance = float('inf')
    next_vertex = None
    for i in range(n):
        if graph[current][i] > 0 and not visited[i]:
            if graph[current][i] < min_distance:
                min_distance = graph[current][i]
                next_vertex = i
    if next_vertex is None:
        print("Hamiltonian cycle does not exist")
        sys.exit()
    path.append(next_vertex)
    visited[next_vertex] = True

price = sum(graph[path[i - 1]][path[i]] for i in range(n))
path_str = " -> ".join(str(vertex) for vertex in path)
print("Price = {}, {}".format(price, path_str + " -> " + str(start)))
