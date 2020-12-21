# n 종류의 화폐. 화폐 개수 최소한 이용해 합 M원 되도록.
n,m = map(int, input().split())

# n 종류 화폐 단위 정보
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기위한 DP 테이블 초기화
d = [10001] * (m+1)

# a_i: 금액 i를 만들 수 있는 최소한의 화폐 개수
# k: 각 화폐의 단위
# 점화식: 각 화폐 단위인 k를 하나씩 돌면서
#    a_i-k를 만드는 방법 존재하는 경우 a_i = min(a_i, a_i-k + 1)
#    a_i-k를 만드는 방법 존재하지 않는 경우 a_i = INF (10001)

# bottom up dp
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001: # (i-k)원을 만드는 방법 존재하는 경우 (코드상으론 j-array[i])
            d[j] = min(d[j], d[j - array[i]] + 1)
            
            
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])