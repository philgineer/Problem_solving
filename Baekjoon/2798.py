n, m = map(int, input().split())
card = list(map(int, input().split()))
res = set()
i = 0
while i < n - 2:    
    j = i + 1
    while j < n - 1:
        k = j + 1
        while k < n:
            if card[i] + card[j] + card[k] <= m:
                res.add(card[i] + card[j] + card[k])
            k += 1
        j += 1
    i += 1
print(max(res))