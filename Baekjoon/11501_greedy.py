import time
from itertools import accumulate
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    acc_list = list(accumulate(prices))
    rev_prices = list(reversed(prices))
    rank = deque()
    profit = 0
    best = 0
    best_idx = 0
    for i, price in enumerate(rev_prices):
        if price > best:
            best = price
            best_idx = n - i - 1
            rank.appendleft(best_idx)
    # print('list:',prices)
    # print('acc: ',acc_list)
    # print('rev: ',rev_prices)
    # print('rank:',rank)

    temp = 0
    prev = 0
    for i in rank:
        if i != 0:
            diff = prices[i] * (i - prev) - (acc_list[i-1] - temp)
            profit += diff
            # print('i - prev:', i - prev)
            # print('acc[i-1] - temp:', acc_list[i-1] - temp)
            # print(f'profit has been added {diff}')
        temp = acc_list[i]
        prev = i + 1
    res.append(profit)

for r in res:
    print(r)