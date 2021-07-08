n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start = 1
end = 1000000
temp = 0
while True:
    mid = (start + end) // 2
    if start > end:
        print(temp)
        break
    cash = mid
    cnt = 1
    min_flag = 0
    for i in arr:
        if i > mid:
            min_flag = 1
            break
        if i <= cash:
            cash -= i
        else:
            cash = mid - i
            cnt += 1
    if min_flag or cnt > m:
        start = mid + 1
    elif cnt <= m:
        temp = mid
        end = mid - 1