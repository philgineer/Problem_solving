import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jew = []
for _ in range(n):
    heapq.heappush(jew, tuple(map(int, input().split())))
bag = [int(input()) for _ in range(k)]
bag.sort()

res = 0
available = []
for b in bag:
    while jew and b >= jew[0][0]:
        heapq.heappush(available, -heapq.heappop(jew)[1])
    if available:
        res += heapq.heappop(available)
    elif not jew:
        break
    
print(-res)