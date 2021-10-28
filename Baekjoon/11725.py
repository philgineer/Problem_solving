import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = [False] * (n+1)
    q = deque([1])
    while q:
        now = q.pop()
        for next in graph[now]:
            if not parent[next]:
                parent[next] = now
                q.append(next)

    return '\n'.join(map(str, parent[2:]))

print(solve())