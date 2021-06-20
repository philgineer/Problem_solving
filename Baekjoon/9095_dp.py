t = int(input())

dp = [1, 2, 4, 0, 0, 0, 0, 0, 0, 0]

def num_case(num):
    if dp[num-1]:
        return dp[num-1]
    else:
        temp = num_case(num-1) + num_case(num-2) + num_case(num-3)
        dp[num-1] = temp
        return temp

for _ in range(t):
    n = int(input())
    print(num_case(n))