import sys
input = sys.stdin.readline

n = int(input())
acc_max = [0, 0, 0]
acc_min = [0, 0, 0]

for _ in range(n):
    input_list = list(map(int, input().split()))
    acc_max = [
        max(acc_max[0], acc_max[1]) + input_list[0],
        max(acc_max[0], acc_max[1], acc_max[2]) + input_list[1],
        max(acc_max[1], acc_max[2]) + input_list[2]
    ]
    acc_min = [
        min(acc_min[0], acc_min[1]) + input_list[0],
        min(acc_min[0], acc_min[1], acc_min[2]) + input_list[1],
        min(acc_min[1], acc_min[2]) + input_list[2]
    ]

print(max(acc_max), min(acc_min))