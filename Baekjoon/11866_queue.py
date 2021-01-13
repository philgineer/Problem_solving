from collections import deque

n, k = map(int, input().split())
q = deque([i + 1 for i in range(n)])
res = []
while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    res.append(str(q.popleft()))
print('<' + ', '.join(res) + '>')