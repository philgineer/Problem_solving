import sys
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    p = input()
    n = int(input())
    arr = eval(input())
    error = False
    forward = 1
    start, end = 0, n
    for i in range(len(p) - 1):
        if p[i] == 'R':
            forward *= -1
        elif p[i] =='D':
            if n:
                if forward == 1:
                    start += 1
                else:
                    end -= 1
                n -= 1
            else:
                error = True
                break
    if error:
        res.append('error')
    elif forward == 1:
        res.append('[' + ','.join(map(str,arr[start:end:forward])) + ']')
    elif start == 0:
        res.append('[' + ','.join(map(str,arr[end-1::forward])) + ']')
    else:
        res.append('[' + ','.join(map(str,arr[end-1:start-1:forward])) + ']')

for r in res:
    print(r)