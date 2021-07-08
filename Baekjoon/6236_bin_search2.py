n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start = max(arr)
end = sum(arr)
temp = 0
while True:
    mid = (start + end) // 2
    if start > end:
        print(temp)
        break
    cash = mid
    cnt = 1
    for i in arr:
        if i <= cash:
            cash -= i
        else:
            cash = mid - i
            cnt += 1
    if cnt > m:
        start = mid + 1
    elif cnt <= m:
        temp = mid
        end = mid - 1