import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
_, *known = map(int, input().split())
tree = [set() for _ in range(n + 1)]
party = []

for _ in range(m):
    _, *people = map(int, input().split())
    for p in people:
        tree[p] |= set(people)
    party.append(people)

q = deque(known)
visited = [False] * (n + 1)
while q:
    now = q.pop()
    if visited[now]:
        continue
    visited[now] = True
    if now not in known:
        known.append(now)
    for next in tree[now]:
        if next != now and not visited[next]:
            q.append(next)

res = 0
for pt in party:
    flag = 0
    for p in pt:
        if p in known:
            flag = 1
            break
    if not flag:
        res += 1

print(res)