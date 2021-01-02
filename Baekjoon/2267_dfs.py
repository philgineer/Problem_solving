def dfs(i, j):
    count = 0
    if i < 0 or i > n - 1 or j < 0 or j > n - 1:
        return count
    if graph[i][j] == 1:
        graph[i][j] = 0
        count += 1
        count += dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
    return count

n = int(input())
graph = []
res = []
num = 0
for _ in range(n):
    graph.append(list(map(int, input())))
for i in range(n):
    for j in range(n):
        count = dfs(i, j)
        if count > 0:
            res.append(count)
            num += 1
res.sort()
print(num)
for r in res:
    print(r)