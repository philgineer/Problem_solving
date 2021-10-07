import sys
input = sys.stdin.readline

s1 = '_' + input().rstrip()
s2 = '_' + input().rstrip()
len1, len2 = len(s1), len(s2)
dp = [[0] * len2 for _ in range(len1)]

for i in range(1, len1):
    for j in range(1, len2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])