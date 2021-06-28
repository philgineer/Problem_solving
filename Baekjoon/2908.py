import sys
input = sys.stdin.readline

i1, i2 = map(int, input().split())
i1 = (i1 % 10) * 100 + (i1 % 100 // 10 * 10) + (i1 % 1000 // 100)
i2 = (i2 % 10) * 100 + (i2 % 100 // 10 * 10) + (i2 % 1000 // 100)
print(max(i1, i2))