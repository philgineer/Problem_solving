from collections import deque

nums = [4, 2, 3, 4, 1, 0, 2, 3]

def jump_to_last(nums):
    last_idx = len(nums) - 1
    visited = [False] * len(nums)
    q = deque()
    q.append((0, 0))

    while q:
        i, cnt = q.popleft()
        if i == last_idx:
            return cnt
        visited[i] = True
        if i - nums[i] >= 0 and visited[i - nums[i]] == False:
            q.append((i - nums[i], cnt + 1))
        if i + nums[i] <= last_idx and visited[i + nums[i]] == False:
            q.append((i + nums[i], cnt + 1))
    return -1

print(jump_to_last(nums))