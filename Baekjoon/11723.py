import sys
input = sys.stdin.readline

m = int(input())
s = []
for _ in range(m):
    inp = input().split()
    if inp[0] == 'all':
        s = [i for i in range(1, 21)]
        continue
    elif inp[0] == 'empty':
        s = []
        continue
    num = int(inp[1])
    if inp[0] == 'add':
        if num not in s:
            s.append(num)
    elif inp[0] == 'remove':
        if num in s:
            s.remove(num)
    elif inp[0] == 'check':
        print(int(num in s))
    elif num in s:
        s.remove(num)
    else:
        s.append(num)