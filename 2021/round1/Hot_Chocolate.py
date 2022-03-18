# https://train.nzoi.org.nz/problems/1195
# Key: Dynamic programming
# Too difficult, come back later.

import math
from operator import itemgetter


L, R = map(int, input().split())
N = int(input())
students = []
happiness = 0
for i in range(N):
    c, l, r = map(int, input().split())
    if l == -1:
        R -= c
        happiness += r
    elif r == -1:
        L -= c
        happiness += l
    else:
        students.append((c, l, r, l / c, r / c))

if (sum((i[0] for i in students)) > L + R
    or L < 0
    or R < 0):
    print("Camp is cancelled.")
    exit()
students = [i + info for i, info in enumerate(students)]
students.sort(key=itemgetter(4), reverse=True)
students2 = sorted(students, key=itemgetter(5), reverse=True)
