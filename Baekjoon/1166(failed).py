import math

n, *lwh = map(int, input().split())

print('lwh:', lwh)
temp = lwh.copy()
a = max(temp)

i = 0 
while True:
    a = max(temp)
    print('a:', a)
    m = math.prod(map(lambda x: x//a, lwh))
    print('m:', m)
    if m >= n:
        break
    for i, val in enumerate(temp):
        if val == a:
            temp[i] = val/2
    print('temp:', temp)