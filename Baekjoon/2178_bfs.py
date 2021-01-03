n, m = map(int, input().split())
graph = []
dist_map = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input())))

queue = [(0,0)]
dist_map[0][0] = 1

while queue:
    i, j = queue.pop(0)
    if i == n - 1 and j == m - 1:
        print(dist_map[i][j])
        break
    graph[i][j] = 0
    if i > 0 and graph[i - 1][j] == 1 and dist_map[i - 1][j] == 0:
        dist_map[i - 1][j] = dist_map[i][j] + 1
        queue.append((i - 1, j))
    if i < n - 1 and graph[i + 1][j] == 1 and dist_map[i + 1][j] == 0:
        dist_map[i + 1][j] = dist_map[i][j] + 1
        queue.append((i + 1, j))
    if j > 0 and graph[i][j - 1] == 1 and dist_map[i][j - 1] == 0:
        dist_map[i][j - 1] = dist_map[i][j] + 1
        queue.append((i, j - 1))
    if j < m - 1 and graph[i][j + 1] == 1 and dist_map[i][j + 1] == 0:
        dist_map[i][j + 1] = dist_map[i][j] + 1
        queue.append((i, j + 1))