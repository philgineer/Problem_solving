import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
t = int(input())
tc = list(map(int, input().split()))

res = ['_'] * t
for i, case in enumerate(tc):
    possible = set()
    possible.add(case)
    for w in weights:
        temp = []
        for diff in [0, -w, w]:
            for p in possible:
                temp.append(p + diff)
            for val in temp:
                possible.add(val)
    if 0 in possible:
        res[i] = 'Y'
    else:
        res[i] = 'N'
print(' '.join(res))