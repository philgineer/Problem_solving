import heapq

n = int(input())
q, res = [], []
while n > 0:
    x = int(input())
    if x > 0:
        heapq.heappush(q, -x)
    if x == 0:
        if q:
            res.append(-heapq.heappop(q))
        else:
            res.append(0)
    n -= 1
for r in res:
    print(r)