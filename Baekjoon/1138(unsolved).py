import sys
input = sys.stdin.readline

n = int(input())
cnt_left = list(map(int, input().split()))
res = [0] * n

for i, c in enumerate(cnt_left):
    res[c] = i + 1
    
print(res)