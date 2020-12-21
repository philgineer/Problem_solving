from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1 - 1].append(n2)
    graph[n2 - 1].append(n1)
for g in graph:
    g.sort()

visited = [False] * n
res = []

def dfs(start):
    visited[start - 1] = True
    res.append(start)
    for child in graph[start - 1]:
        if visited[child - 1] == False:
            dfs(child)
            
queue = deque()

def bfs(start):
    visited = [False] * n
    visited[start - 1] = True
    print(start, end=' ')
    for child in graph[start - 1]:
        queue.append(child)
        visited[child - 1] = True
    while queue:
        pop = queue.popleft()
        if queue:
            print(pop, end=' ')
        else:
            print(pop)
        for child in graph[pop - 1]:
            if visited[child - 1] == False:
                queue.append(child)
                visited[child - 1] = True
        
dfs(v)
for i, r in enumerate(res):
    if i == len(res) - 1:
        print(r)
    else:
        print(r, end=' ')
bfs(v)