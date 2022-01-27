import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = l[i]
    else:
        dp[i] = max(l[i], dp[i-1] + l[i])
        
print(max(dp))