import sys
input = sys.stdin.readline

def in_circle(point, circle):
    x, y = point
    cx, cy, r = circle
    return (x - cx) ** 2 + (y - cy) ** 2 < r ** 2


t = int(input())
for _t in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = []
    for _n in range(n):
        planets.append(list(map(int, input().split())))
    diff_circle = []
    for planet_idx, planet in enumerate(planets):
        if in_circle([x1, y1], planet):
            diff_circle.append(planet_idx)
        if in_circle([x2, y2], planet):
            if planet_idx in diff_circle:
                diff_circle.remove(planet_idx)
            else:
                diff_circle.append(planet_idx)
    print(len(diff_circle))