def hanoi_solver(disks):
    rods = [list(range(disks, 0, -1)), [], []]
    moves = [f"{rods[0]} {rods[1]} {rods[2]}"]

    def solve(disk, source, support, destination):
        if disk == 0:
           return

        solve(disk - 1, source, destination, support)

        tomove = rods[source].pop()
        rods[destination].append(tomove)
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

        solve(disk - 1, support, source, destination)

    solve(disks, 0, 1, 2)
    return "\n".join(moves).strip()

print(hanoi_solver(5))
