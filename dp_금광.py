# array[i][j]: i행 j열에 존재하는 금의 양
# dp[i][j]: i행 j열까지의 최적의 해 (얻을 수 있는 금의 최댓값)
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

# test case 입력 (n * m 크기의 금광)
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    dp = []
    index = 0
    
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
        
    # dynamic programming
    for j in range(1, m):
        for i in range(n):
            
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: left_down = 0
            else: left_down = dp[i+1][j-1]
            
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
            
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)