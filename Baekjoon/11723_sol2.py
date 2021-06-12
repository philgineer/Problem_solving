"""
Bit mask로 시도했지만 오히려 시간이 더 오래 걸려 시간 초과 판정.
"""

import sys
input = sys.stdin.readline

m = int(input())
s = [0] * 20
for _ in range(m):
    inp = input().split()
    if inp[0] == 'all':
        for i in range(20):
            s[i] |= 1
        continue
    elif inp[0] == 'empty':
        for i in range(20):
            s[i] &= 0
        continue
    num = int(inp[1]) - 1
    if inp[0] == 'add':
        s[num] |= 1
    elif inp[0] == 'remove':
        s[num] &= 0
    elif inp[0] == 'check':
        print(s[num])
    else:
        s[num] ^= 1