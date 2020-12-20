from collections import deque

n = int(input())
queue = deque(i + 1 for i in range(n))
i = 0
while len(queue) > 1:
    if i % 2 == 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    i += 1
print(queue[0])