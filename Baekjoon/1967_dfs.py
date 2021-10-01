import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(node, dist):
    visited[node] = True
    distance[node] = dist
    for next_node, cost in tree[node]:
        if not visited[next_node]:
            dfs(next_node, dist + cost)

n = int(input())
tree = [[] for _ in range(n+1)]
distance = [0] * (n+1)

for _ in range(n-1):
    parent, child, cost = map(int, input().split())
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))

visited = [False] * (n+1)
dfs(1, 0)
idx = distance.index(max(distance))
visited = [False] * (n+1)
dfs(idx, 0)
print(max(distance))