import heapq
import sys
input = sys.stdin.readline
INF = 123456789

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
t_start, t_end = map(int, input().split())
distance = [INF] * (n + 1)
distance[t_start] = 0

heap = []
heapq.heappush(heap, (0, t_start))
while heap:
    dist, now = heapq.heappop(heap)
    if distance[now] < dist:
        continue
    for node, cost in graph[now]:
        if dist + cost < distance[node]:
            distance[node] = dist + cost
            heapq.heappush(heap, (dist + cost, node))

print(distance[t_end])