n, m = map(int, input().split())
trees = list(map(int, input().split()))

res = 0
start = 0
end = max(trees)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in trees:
        total += max(0, tree - mid)
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)