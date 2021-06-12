import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s1, s2 = set(), set()
for _ in range(n):
    s1.add(input().rstrip())
for _ in range(m):
    s2.add(input().rstrip())
res = sorted(list(s1 & s2))
print(len(res))
for r in res:
    print(r)