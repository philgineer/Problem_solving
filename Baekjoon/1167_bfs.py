import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (n+1)
    q = deque()
    q.append((start, 0))
    while q:
        now, dist = q.pop()
        distance[now] = dist
        visited[now] = True
        for next_node, cost in tree[now]:
            if not visited[next_node]:
                q.append((next_node, dist + cost))

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

bfs(1)
idx = distance.index(max(distance))
bfs(idx)
print(max(distance))