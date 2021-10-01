import sys
from collections import deque
from heapq import heapq
input = sys.stdin.readline

def get_max_dist(node):
    q = deque()
    visited = [False] * (n+1)
    q.append((node, 0))
    distance = [0] * (n+1)
    while q:
        now, dist = q.pop()
        if visited[now]:
            continue
        visited[now] = True
        distance[now] = dist
        for next_node, cost in tree[now]:
            if not visited[next_node]:
                q.append((next_node, dist + cost))
    return max(distance)

n = int(input())
tree = [[] for _ in range(n+1)]
is_edge = [0] + [1] * n

for _ in range(n-1):
    parent, child, cost = map(int, input().split())
    is_edge[parent] = 0
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))

edge = [idx for idx, val in enumerate(is_edge) if val == 1]
best = 0
for i in range(1, n):
    if i in edge:
        res = get_max_dist(i)
        if best < res:
            best = res

print(best)
