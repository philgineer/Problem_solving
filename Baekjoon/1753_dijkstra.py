import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = int(1e9)
distance = [INF] * (V + 1)
distance[k] = 0
heap = []
heapq.heappush(heap, (0, k))
while heap:
    dist, now = heapq.heappop(heap)
    if distance[now] < dist:
        continue
    for node, cost in graph[now]:
        if dist + cost < distance[node]:
            distance[node] = dist + cost
            heapq.heappush(heap, (dist + cost, node))

for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)