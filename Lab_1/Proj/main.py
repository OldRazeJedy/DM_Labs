import heapq
import sys

input_file = ""

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    print("No input file specified!")
    exit()

with open(input_file, "r") as f:
    n = int(f.readline().strip())
    matrix = []
    for i in range(n):
        row = list(map(int, f.readline().strip().split()))
        matrix.append(row)


    def _prim_mst(adj_matrix, sign):
        num_vertices = len(adj_matrix)
        visited = [False] * num_vertices
        mst_edges = []
        parents = [-1] * num_vertices
        min_heap = [(0, 0, -1)]
        while min_heap:
            weight, vertex, parent = heapq.heappop(min_heap)
            if not visited[vertex]:
                visited[vertex] = True
                parents[vertex] = parent
                for neighbor, neighbor_weight in enumerate(adj_matrix[vertex]):
                    if neighbor_weight > 0 and not visited[neighbor]:
                        heapq.heappush(min_heap, (neighbor_weight * sign, neighbor, vertex))
                if vertex != 0:
                    mst_edges.append((min(vertex, parent), max(vertex, parent), weight * sign))
        return mst_edges


    def prim_mst_min(adj_matrix):
        return _prim_mst(adj_matrix, 1)


    def prim_mst_max(adj_matrix):
        return _prim_mst(adj_matrix, -1)


    min_tree = prim_mst_min(matrix)
    max_tree = prim_mst_max(matrix)

    print("Minimum spanning tree weight:", min_tree)
    print("Maximum spanning tree weight:", max_tree)