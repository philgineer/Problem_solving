n = int(input())

dp = [0.] * n
num = float(input())
dp[0] = num

for i in range(1, n):
    num = float(input())
    dp[i] = max(num, dp[i-1] * num)
    
print('{:.3f}'.format(max(dp)))