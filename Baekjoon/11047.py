n, k = map(int, input().split())
X = [int(input()) for _ in range(n)]
X.sort(reverse=True)
coin_num = 0
for i in X:
    num = k // i
    left = k % i
    coin_num += num
    k = left
print(coin_num)