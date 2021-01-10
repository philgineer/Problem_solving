n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
arr.sort()
res = []

def bi_search(start, end):
    if end < start:
        res.append(0)
        return
    if arr[(start + end) // 2] == num:
        res.append(1)
        return
    elif arr[(start + end) // 2] > num:
        bi_search(start, (start + end) // 2 - 1)
    else:
        bi_search((start + end) // 2 + 1, end)

for i, num in enumerate(find):
    bi_search(0, n-1)
    print(res[i])