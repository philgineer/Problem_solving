from collections import deque

m_list = []
q_list = []
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    m_list.append(m)
    q_list.append(deque(map(int, input().split())))

def is_head_biggest(b_list):
    for i in b_list:
        if i > b_list[0]:
            return False
    return True
    
i = 0
for q in q_list:
    find = m_list[i]
    cnt = 1
    j = 0
    while len(q) >= 1:
        if (is_head_biggest(q)):
            if j == find:
                print(cnt)
                break
            q.popleft()
            cnt += 1
        else:
            q.append(q.popleft())
            if j == find:
                j = -1
                find = len(q) - 1
        j += 1
    i += 1