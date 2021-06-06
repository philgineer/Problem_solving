nums = [int(input()) for i in range(10)]
print(len(set(map(lambda x: x % 42, nums))))