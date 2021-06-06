nums = [int(input()) for i in range(3)]
mul = str(nums[0] * nums[1] * nums[2])
res = [0 for i in range(10)]
for m in mul:
    res[int(m)] += 1
for r in res:
    print(r)