n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]

houses.sort()

print(houses)

if c == 2:
    print(houses[-1] - houses[0])

start = 1
end = len(houses) - 2
while (start <= end):
    mid = (start + end) // 2
    closest = 0
    for i in range(end - start):
        houses[]
