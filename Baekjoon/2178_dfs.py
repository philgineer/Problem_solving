def dfs(i, j, count, graph):
    if i == n - 1 and j == m - 1:
        res.append(count)
        return
    if graph[i][j] == 1:
        buff_graph = [[] for _ in range(n)]
        for _i in range(n):
            for _j in range(m):
                buff_graph[_i].append(graph[_i][_j])
        buff_graph[i][j] = 0
        if i > 0:
            dfs(i - 1, j, count + 1, buff_graph)
        if i < n - 1:
            dfs(i + 1, j, count + 1, buff_graph)
        if j > 0:
            dfs(i, j - 1, count + 1, buff_graph)
        if j < m - 1:
            dfs(i, j + 1, count + 1, buff_graph)
    return

n, m = map(int, input().split())
init_graph = []
res = []
for _ in range(n):
    init_graph.append(list(map(int, input())))
dfs(0, 0, 1, init_graph)
print(min(res))