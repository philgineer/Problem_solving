import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
dp_rev = [1] * n
for i in range(1, n):
    for j in range(1, i + 1):
        if arr[i] > arr[i - j]:
            dp[i] = max(dp[i], dp[i - j] + 1)
        if arr[n-1 - i] > arr[n-1 - i + j]:
            dp_rev[n-1 - i] = max(dp_rev[n-1 - i], dp_rev[n-1 - i + j] + 1)

max_val = 0
for i in range(n):
   if dp[i] + dp_rev[i] > max_val:
       max_val = dp[i] + dp_rev[i]

print(max_val - 1)