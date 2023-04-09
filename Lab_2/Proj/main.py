import sys
import copy


def read_matrix(filename):
    with open(filename) as f:
        n = int(f.readline())
        matrix = []
        for i in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
        return matrix, n


def eulerian_path_or_cycle(matrix, n):
    if any(sum(1 for x in w if x > 0) % 2 == 1 for w in matrix):
        return None

    path = []
    stack = [0]
    copy_matrix = copy.deepcopy(matrix)
    while stack:
        vertex = stack[-1]
        if any(copy_matrix[vertex]):
            next_vertex = min([i for i, v in enumerate(copy_matrix[vertex]) if v])
            stack.append(next_vertex)
            copy_matrix[vertex][next_vertex] = 0
            copy_matrix[next_vertex][vertex] = 0
        else:
            path.append(stack.pop())

    path.reverse()
    return path


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    matrix, n = read_matrix(filename)
    path = eulerian_path_or_cycle(matrix, n)
    if path is None:
        print("No Eulerian path or cycle")
    else:
        cost = sum(matrix[path[i]][path[i+1]] for i in range(len(path)-1))
        print(f"Total cost = {cost}")
        print("Traversal sequence:", " --> ".join(str(x) for x in path))
