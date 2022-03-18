# https://train.nzoi.org.nz/problems/1166

import math

N, T = map(int, input().split())
boxes = list(map(int, input().split()))
counts = [0] * 100001
for box in boxes:
    counts[box] += 1

mean = math.floor(sum(boxes) / N)
time = T
j = 100000
for i in range(1, mean + 1):
    minchange = min(counts[i], time)
    counts[i + 1] += minchange
    counts[i] -= minchange
    time -= minchange
    while minchange > 0:
        while counts[j] == 0:
            j -= 1
        maxchange = min(counts[j], minchange)
        counts[j - 1] += maxchange
        counts[j] -= maxchange
        minchange -= maxchange

smallest = min((i for i, count in enumerate(counts) if count > 0))
largest = max((i for i, count in enumerate(counts) if count > 0))
print(largest - smallest)