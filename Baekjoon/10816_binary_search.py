from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
arr.sort()

for i in range(m - 1):
    print(bisect_right(arr, find[i]) - bisect_left(arr, find[i]), end=' ')
print(bisect_right(arr, find[m - 1]) - bisect_left(arr, find[m - 1]))