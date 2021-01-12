k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
res = 1
start = 1
end = max(arr)
while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for num in arr:
        cnt += num // mid
    if n > cnt:
        end = mid - 1
    else:
        start = mid + 1
        res = mid
print(res)