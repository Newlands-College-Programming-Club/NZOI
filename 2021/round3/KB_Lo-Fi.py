revenue = 0

N = int(input())
bids = []
for i in range(N):
    bids.append(int(input()))
bids.sort(reverse=True)

M = int(input())
prices = []
for i in range(M):
    prices.append(int(input()))
prices.sort(reverse=True)

i = 0
j = 0
while i < M and j < N:
    if prices[i] > bids[j]:
        i += 1
    else:
        revenue += prices[i]
        i += 1
        j += 1

print(revenue)