n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
visited = [False] * (n + 1)

def dfs(start = 1):
    visited[start] = True
    for child in graph[start]:
        if visited[child] == False:
            dfs(child)
            
dfs()
print(sum(visited) - 1)