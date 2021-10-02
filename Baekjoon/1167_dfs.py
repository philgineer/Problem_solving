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

for _ in range(n):
    input_list = list(map(int, input().split()))
    parent = input_list[0]
    i = 1
    while True:
        if input_list[i] == -1:
            break
        child, cost = input_list[i], input_list[i+1]
        tree[parent].append((child, cost))
        tree[child].append((parent, cost))
        i += 2

visited = [False] * (n+1)
dfs(1, 0)
idx = distance.index(max(distance))
visited = [False] * (n+1)
dfs(idx, 0)
print(max(distance))