import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def bfs(v_from, v_to):
    heap = []
    heapq.heappush(heap, (0, v_from))
    distance = [INF] * (n + 1)
    distance[v_from] = 0
    while heap:
        dist, start = heapq.heappop(heap)
        if distance[start] < dist:
            continue
        for next, cost in graph[start]:
            if dist + cost < distance[next]:
                distance[next] = dist + cost
                heapq.heappush(heap, (dist + cost, next))
    return distance[v_to]


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

path1 = bfs(1, v1) + bfs(v1, v2) + bfs(v2, n)
path2 = bfs(1, v2) + bfs(v2, v1) + bfs(v1, n)
res = min(path1, path2)
if res < INF:
    print(res)
else:
    print(-1)