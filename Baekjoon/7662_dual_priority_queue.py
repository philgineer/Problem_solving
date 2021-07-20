import heapq
import sys
input = sys.stdin.readline

def safe_pop(q):
    ret = None
    while q:
        val, idx = heapq.heappop(q)
        if is_in_q[idx]:
            is_in_q[idx] = False
            ret = val
            break
    return ret

for testcase in range(int(input())):
    k = int(input())
    q_max, q_min = [], []
    is_in_q = [False] * 1000001
    for i in range(k):
        op, num = input().split()
        if op == 'I':
            heapq.heappush(q_max, (-int(num), i))
            heapq.heappush(q_min, (int(num), i))
            is_in_q[i] = True
        elif op == 'D':
            if num == '1' and q_max:
                safe_pop(q_max)
            elif num == '-1' and q_min:
                safe_pop(q_min)
    res1, res2 = safe_pop(q_max), safe_pop(q_min)
    if res1 == None and res2 == None:
        print('EMPTY')
    else:
        if res2 == None:
            res2 = -res1
        print('{} {}'.format(-res1, res2))