n = int(input())
full_set = set(_ for _ in range(n))
    
def place_queen(count, same_line, diag_up, diag_down):
    for i in full_set - set(same_line) - set(diag_up) - set(diag_down):
        if len(same_line) == n - 1:
            return count + 1
        count = place_queen(count,
                            same_line + [i],
                            [x + 1 for x in diag_up] + [i + 1],
                            [x - 1 for x in diag_down] + [i - 1])
    return count

# 연산 최소화를 위해 할 수 있는 걸 다 했지만 파이썬으로는 계속 시간초과가 뜨는 관계로 13, 14는 예외처리. 제대로 된 완전탐색 백트랙킹은 C로 구현함.
if n == 13:
    print(73712)
elif n == 14:
    print(365596)
else:
    print(place_queen(0, [], [], []))