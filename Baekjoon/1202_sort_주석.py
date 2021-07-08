import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jew = [tuple(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
bag.sort()

print('bag:', bag)

jew.sort(key=lambda x: x[1], reverse=True)

print('jew:', jew)

acc = 0
for m, v in jew:
    flag = 0
    for i in range(len(bag)):
        if bag[i] >= m: # can be put in the bag
            flag = 1
            break
    if not flag: # no bag which is fit
        continue
    print('i:',i)
    # put that jew in the smallest bag which is fit
    acc += v
    temp = bag.pop(i)
    print('jew (m: {}, v: {}) is put in bag size of {}'.format(m, v, temp))
    print('bag:', bag)
    if not bag:
        break

print('total values:', acc)