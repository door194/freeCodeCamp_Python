def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []

    def dfs(row, cols, diagonals, anti_diagonals, board):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if (col in cols or
                (row - col) in diagonals or
                (row + col) in anti_diagonals):
                continue

            cols.add(col)
            diagonals.add(row - col)
            anti_diagonals.add(row + col)
            board.append(col)

            dfs(row + 1, cols, diagonals, anti_diagonals, board)

            board.pop()
            cols.remove(col)
            diagonals.remove(row - col)
            anti_diagonals.remove(row + col)

    dfs(0, set(), set(), set(), [])
    return solutions
