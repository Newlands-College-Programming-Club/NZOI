# https://train.nzoi.org.nz/problems/1222

N = int(input())
M = int(input())

import bisect

def place(a, x):
    'Locate the rightmost value less than x'
    i = bisect.bisect_left(a, x)
    # No contestants are unofficial.
    if len(a) == 0:
        return x
    elif i != len(a) and a[i] == x:
        return "UNOFFICIAL"
    # A number of unofficial contestants are in front of x.
    else:
        return x - i

def toggle(a: list, x):
    'Locate the leftmost exact location of x.'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        a.pop(i)
    else:
        a.insert(i, x)

unofficial = []
output = []

for i in range(M):
    line = input().split()
    if line[0] == "t":
        toggle(unofficial, int(line[-1]))
    else:
        output.append(place(unofficial, int(line[-1])))

for line in output:
    print(line)