import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 10000
for _ in range(n):
    arr[int(input())-1] += 1
for i in range(10000):
    while arr[i] >= 1:
        print(i+1)
        arr[i] -= 1