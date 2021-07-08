n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1
if arr[1] > arr[0]:
    dp[1] = 2
else:
    dp[1] = 1

temp = 1
backward = 1
for i in range(2, n):
    for j in range(backward, i+1):
        #print('i:',i,'j:',j,'flag:',backward)
        if arr[i] > arr[i - j]:
            dp[i] = max(dp[i], dp[i - j] + 1)
    if dp[i-1] == backward and arr[i] > arr[temp-1]:
        print('dp[i-1] == backward', dp[i-1], backward)
        dp[i] = max(dp[i], dp[i-1] + 1)
        backward = 1
    elif dp[i] < dp[i-1]:
        print('flag! dp[{}] is less than dp[{}]!'.format(i, i-1))
        dp[i] = dp[i-1]
        backward += 1
        temp = i
    else:
        backward = 1

print(' '.join(str(x) for x in dp))
print(dp[n-1])