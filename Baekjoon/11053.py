n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(1, i+1):
        if arr[i] > arr[i - j]:
            dp[i] = max(dp[i], dp[i - j] + 1)

print(max(dp))