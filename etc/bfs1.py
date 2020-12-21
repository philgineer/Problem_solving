import sys
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1 ### 이런 방법이!!!

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())

graph = []
for i in range(n+1):
    graph.append([])

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    # graph[b].append(a) ### 단방향 도로임!!!

visited = [False] * (n+1)
distance = [0] * (n+1)

bfs(graph, x)

for i in range(n+1):
    if distance[i] == k:
        print(i)
if k not in distance:
    print(-1)