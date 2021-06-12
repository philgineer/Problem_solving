import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic_s = {}
dic_i = [0] * n
for i in range(n):
    s = input().rstrip()
    dic_s[s] = i
    dic_i[i] = s
for i in range(m):
    q = input().rstrip()
    if q.isalpha():
        print(dic_s[q] + 1)
    else:
        print(dic_i[int(q) - 1])