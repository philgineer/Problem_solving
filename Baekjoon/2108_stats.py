import sys
input = sys.stdin.readline

n = int(input())
l = [0] * n
count = [0] * 8001

acc = 0
for i in range(n):
    num = int(input())
    l[i] = num
    count[num + 4000] += 1
    acc += num

temp = abs(max(l) - min(l))
l.sort()
most = max(count)
most_nums = [i - 4000 for i, x in enumerate(count) if x == most]
print(round(acc/n))
print(l[n//2])
if len(most_nums) > 1:
    print(most_nums[1])
else:
    print(most_nums[0])
print(temp)