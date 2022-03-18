# https://train.nzoi.org.nz/problems/1132

import bisect

N, K = map(int, input().split())
space = []
for _ in range(N):
    space.append([False] * K)
# Not using the following line. The rows points to the same object.
# space = [[False] * K] * (N + 1)
# print(id(space[0]), id(space[1]))
row = 0
top = 0
for i in range(N):
    row = top
    width = int(input())
    pos = K - width
    # Find the row that cannot pass.
    while row > 0 and (not space[row - 1][pos]):
        row -= 1
    # Add to the row above.
    pos = space[row].index(False)
    space[row][pos:pos+width] = [True] * width
    top += 1 if any(space[top]) else 0

row = 0
while any(space[row]):
    row += 1

layers = []
gaps = []
for j in range(N):
    width = int(input())
    i = bisect.bisect_right(gaps, width) - 1
    i2 = bisect.bisect_right()
print(row)