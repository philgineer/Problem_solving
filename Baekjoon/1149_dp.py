import sys
sys.setrecursionlimit(10000)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [(0, 0, 0) for _ in range(n + 1)]

def get_min_sofar(k):
    if dp[k] != (0, 0, 0):
        return dp[k]
    r, g, b = arr[k - 1]
    if k == 1:
        dp[1] = r, g, b
        return r, g, b
    pre_r, pre_g, pre_b = get_min_sofar(k - 1)
    curr_r = min(pre_g, pre_b) + r
    curr_g = min(pre_r, pre_b) + g
    curr_b = min(pre_r, pre_g) + b
    dp[k] = curr_r, curr_g, curr_b
    return curr_r, curr_g, curr_b

print(min(get_min_sofar(n)))