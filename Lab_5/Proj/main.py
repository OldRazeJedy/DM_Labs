import sys


def read_adj_matrix(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    n = len(lines)
    adj_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        row = lines[i].split()
        for j in range(n):
            adj_matrix[i][j] = int(row[j])
    return adj_matrix


def is_isomorphic(adj_matrix1, adj_matrix2):
    n = len(adj_matrix1)
    for perm in get_all_permutations(n):
        if is_permutation_valid(adj_matrix1, adj_matrix2, perm):
            return True, perm
    return False, None


def get_all_permutations(n):
    used = [False] * n
    perm = [0] * n
    result = []
    generate_permutations(n, 0, used, perm, result)
    return result


def generate_permutations(n, i, used, perm, result):
    if i == n:
        result.append(perm[:])
        return
    for j in range(n):
        if not used[j]:
            used[j] = True
            perm[i] = j
            generate_permutations(n, i + 1, used, perm, result)
            used[j] = False


def is_permutation_valid(adj_matrix1, adj_matrix2, perm):
    adj_matrix3 = permute_adj_matrix(adj_matrix1, perm)
    return are_adj_matrices_equal(adj_matrix2, adj_matrix3)


def permute_adj_matrix(adj_matrix, perm):
    n = len(adj_matrix)
    adj_matrix_perm = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            adj_matrix_perm[perm[i]][perm[j]] = adj_matrix[i][j]
    return adj_matrix_perm


def are_adj_matrices_equal(adj_matrix1, adj_matrix2):
    n = len(adj_matrix1)
    for i in range(n):
        for j in range(n):
            if adj_matrix1[i][j] != adj_matrix2[i][j]:
                return False
    return True


def modify_graph(adj_matrix, perm):
    global is_isomorphic
    n = len(adj_matrix)
    for u in range(n):
        for v in range(u + 1, n):
            adj_matrix[u][v] = 1 - adj_matrix[u][v]
            adj_matrix[v][u] = 1 - adj_matrix[v][u]
            for x in range(n):
                for y in range(x + 1, n):
                    if x != u and y != v and x != v and y != u:
                        adj_matrix[x][y] = 1 - adj_matrix[x][y]
                        adj_matrix[y][x] = 1 - adj_matrix[y][x]
            is_isomorphic, _ = is_isomorphic(adj_matrix, adj_matrix)
            if not is_isomorphic:
                return adj_matrix
            adj_matrix = permute_adj_matrix(adj_matrix, perm)


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py data1.txt data22.txt")
        return

    adj_matrix1 = read_adj_matrix(sys.argv[1])
    adj_matrix2 = read_adj_matrix(sys.argv[2])

    is_iso, perm = is_isomorphic(adj_matrix1, adj_matrix2)

    if is_iso:
        print("Isomorphism exists with permutation", perm)
    else:
        if perm is not None:
            adj_matrix_modified = modify_graph(adj_matrix1, perm)
            is_iso, perm = is_isomorphic(adj_matrix_modified, adj_matrix2)

            if is_iso:
                print("Isomorphism can be obtained with permutation", perm)
            else:
                print("No isomorphism exists")
        else:
            print("Does not exist and cannot be found")


if __name__ == '__main__':
    main()
