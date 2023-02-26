import sys
input = sys.stdin.readline

a, b = map(int, input().split())

dp_prime: list[bool] = [True] * 100001
dp_prime[0] = False
dp_prime[1] = False
dp_cnt: list[int] = [0] * (b+1)

for i in range(2, 100001):
    if dp_prime[i]:
        for j in range(2, b+1):
            num = i*j
            if num > b:
                break
            dp_prime[num] = False
            temp = num
            while temp % i == 0:
                temp /= i
                dp_cnt[num] += 1

cnt = 0
for i in range(a, b+1):
    if dp_prime[dp_cnt[i]]:
        cnt += 1
print(cnt)