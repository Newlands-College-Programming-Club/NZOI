# https://train.nzoi.org.nz/problems/1207

import math

S = input()
N = int(S)

# 10 has one three
# 100 has 10 (each ten) + 10 (30s)
# 1000 has 20 (each 100) * 10 (number of 100s) + 100 (300s)
# 10000 has 10 * 300 + 1000

digits = math.floor(math.log10(N))
count = 0
for i in range(digits + 1):
    j = (digits - i) * (10 ** (digits - i - 1)) * int(S[i])
    if S[i] == "3":
        if i < len(S) - 1:
            j += int(S[i + 1:]) + 1
        else:
            j += 1

    if int(S[i]) > 3:
        j += 10 ** (digits - i)
    count += j

print(int(count))