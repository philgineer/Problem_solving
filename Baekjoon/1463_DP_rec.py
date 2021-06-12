"""
백준에서 메모리 초과가 떴지만, 시간 복잡도 면에서는
for i in range(2, n+1)로 dp 테이블 다 채우는 코드보다 빠른 코드.
"""

import sys
sys.setrecursionlimit(1000000)
n = int(input())

cnt = 0
dp = [0] * (n+1)

def min_cnt(num):
    if dp[num] or num == 1:
        return dp[num]
    dp[num] = min_cnt(num-1) + 1
    if num % 3 == 0 and min_cnt(num//3) + 1 < dp[num]:
        # print('{} -> {} ({})'.format(num, num//3, min_cnt(num//3)))
        dp[num] = min_cnt(num//3) + 1
    if num % 2 == 0 and min_cnt(num//2) + 1 < dp[num]:
        # print('{} -> {} ({})  ---VS---  {} -> {} ({})'.format(num, num//2, min_cnt(num//2), num,  num-1, min_cnt(num-1)))
        dp[num] = min_cnt(num//2) + 1
    return dp[num]

print(min_cnt(n))
# print(dp)