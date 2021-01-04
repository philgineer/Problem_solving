from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
temp = []
cnt = 0
flag = 0

i_diff = [0, 0, -1, 1]
j_diff = [-1, 1, 0, 0]

# no tomato of 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = 1
            break

# init
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

while flag:
    for t in temp:
        queue.append(t)
    temp = []
    while queue:
        i, j = queue.popleft()
        graph[i][j] = 2
        for idx in range(4):
            new_i = i + i_diff[idx]
            new_j = j + j_diff[idx]
            if 0 <= new_i < n and 0 <= new_j < m and graph[new_i][new_j] == 0:
                graph[new_i][new_j] = 1
                temp.append((new_i,new_j))
    if not temp:
        break
    cnt += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt = -1
            break
if flag == 0:
    cnt = 0
print(cnt)