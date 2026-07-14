def adjacency_list_to_matrix(adj_list):
    # Number of nodes
    n = len(adj_list)

    # Create an n x n matrix filled with 0s
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the matrix based on the adjacency list
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    # Print each row
    for row in matrix:
        print(row)

    # Return the adjacency matrix
    return matrix
