def dfs(graph, root):
    visited = []
    stack = [root]
    seen = [False] * len(graph)

    while stack:
        node = stack.pop()

        if not seen[node]:
            seen[node] = True
            visited.append(node)

            # Push neighbors in reverse order so lower-index nodes
            # are visited first.
            for i in range(len(graph[node]) - 1, -1, -1):
                if graph[node][i] == 1 and not seen[i]:
                    stack.append(i)

    return visited
