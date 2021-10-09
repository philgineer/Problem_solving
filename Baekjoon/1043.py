import sys
input = sys.stdin.readline

n, m = map(int, input().split())
_, *known = map(int, input().split())
known = set(known)
tree = [set() for _ in range(n + 1)]
party = []

for _ in range(m):
    _, *people = map(int, input().split())
    for p in people:
        tree[p] |= set(people)
    party.append(people)

temp = set()
known_prev = set()
while known_prev != known:
    known_prev = known.copy()
    for k in known:
        for connected in tree[k]:
            temp.add(connected)
    known |= temp

res = 0
for pt in party:
    flag = 0
    for p in pt:
        if p in known:
            flag = 1
            break
    if not flag:
        res += 1

print(res)