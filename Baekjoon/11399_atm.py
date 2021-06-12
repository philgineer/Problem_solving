n = int(input())
l = list(map(int, input().split()))

l.sort()
prev = 0
res = 0
for i in l:
    prev += i
    res += prev
#     print('i:',i,'sum:',res)

# print(l)
print(res)