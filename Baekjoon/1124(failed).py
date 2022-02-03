a, b = map(int, input().split())

dp = [1] * 100001
# dp = [0] * 100001

def is_prime(num):
    if num in [0, 1]:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

for i in range(2, int(100000 ** 0.5) + 1):
    j = 2
    while i*j < 100001:
        dp[i*j] = dp[i] * dp[j]
        j += 1

cnt = 0
for num in range(a, b+1):
    cnt += is_prime(dp[num])

print(cnt)
print(dp[:20])