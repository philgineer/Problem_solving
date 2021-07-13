import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

left = 0
right = house[-1]
res = 0
while left <= right:
    mid = (left + right) // 2
    cnt = c - 1
    temp = house[0]
    for i in range(1, n):
        if house[i] - temp >= mid:
            cnt -= 1
            temp = house[i]
        if cnt == 0:
            break
    if cnt:
        right = mid - 1
    else:
        res = mid
        left = mid + 1
print(res)