import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [0] * n
for i in range(n):
    dp[n] = A[n]

for i in range(1, n):
    for j in range(1, i+1):
        if A[i-j] < A[i]:
            dp[i] = max()

    dp[i] = max(acc + A[i], dp[i-1] + A[j])

    
print(dp)