import sys
import heapq

input = sys.stdin.readline
INF = 1e9

def dijkstra(graph, distance, c):
    distance[c] = 0
    heap = []
    heapq.heappush(heap, (0, c))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for cost, next in graph[now]:
            if distance[next] > dist + cost:
                distance[next] = dist + cost
                heapq.heappush(heap, (dist + cost, next))

t = int(input())
for tc in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))
    distance = [INF] * (n + 1)

    dijkstra(graph, distance, c)
    cnt = n + 1
    temp = 0
    for d in distance:
        if d == INF:
            cnt -= 1
        elif d > temp:
            temp = d
    
    print(cnt, temp)