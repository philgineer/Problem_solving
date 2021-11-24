def solve(digit):
    l = []
    for i in range(10):
        if digit < 2:
            l.append(i)
            continue
        for j in range(i):
            if digit < 3:
                l.append(int(f'{i}{j}'))
                continue
            for k in range(j):
                if digit < 4:
                    l.append(int(f'{i}{j}{k}'))
                    continue
                for i2 in range(k):
                    if digit < 5:
                        l.append(int(f'{i}{j}{k}{i2}'))
                        continue
                    for j2 in range(i2):
                        if digit < 6:
                            l.append(int(f'{i}{j}{k}{i2}{j2}'))
                            continue
                        for k2 in range(j2):
                            if digit < 7:
                                l.append(int(f'{i}{j}{k}{i2}{j2}{k2}'))
                                continue
                            for i3 in range(k2):
                                if digit < 8:
                                    l.append(int(f'{i}{j}{k}{i2}{j2}{k2}{i3}'))
                                    continue
                                for j3 in range(i3):
                                    if digit < 9:
                                        l.append(int(f'{i}{j}{k}{i2}{j2}{k2}{i3}{j3}'))
                                        continue
                                    for k3 in range(j3):
                                        if digit < 10:
                                            l.append(int(f'{i}{j}{k}{i2}{j2}{k2}{i3}{j3}{k3}'))
                                            continue
                                        for i4 in range(k3):
                                            if digit < 11:
                                                l.append(int(f'{i}{j}{k}{i2}{j2}{k2}{i3}{j3}{k3}{i4}'))
    return l, len(l)


n = int(input())
if n > 1023:
    print(-1)
else:
    i = 1
    acc = 0
    while True:
        nums, length = solve(i)
        acc += length
        if acc >= n:
            acc -= length
            break
        i += 1
    print(nums[n - acc - 1])