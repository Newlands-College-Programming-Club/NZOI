# https://train.nzoi.org.nz/problems/1133
# Key to the problem, A* algorithm with priority queue.
# Starting from 0, rather than the starting points of every player.

import math
import heapq


class heap(list):
    def __init__(self) -> None:
        self.n = 0

    def __swim(self, k: int) -> None:
        parent = math.ceil(k / 2) - 1
        while (k > 0 and self.__less(k, parent)):
            self.__exchange(k, parent)
            k = parent
            parent = math.ceil(k / 2) - 1

    def __sink(self, k: int) -> None:
        while (k * 2 < self.n - 1):
            j = k * 2 + 1
            if j < self.n - 1 and self.__less(j + 1, j):
                j += 1
            if not self.__less(j, k):
                break
            self.__exchange(k, j)
            k = j

    def __less(self, i: int, j: int) -> bool:
        if self[i][0] < self[j][0]:
            return True
        if self[i][0] == self[j][0]:
            return self[i][1] < self[j][1]
        return False

    def __exchange(self, i: int, j: int) -> None:
        self[i], self[j] = self[j], self[i]

    def heapadd(self, item):
        self.append(item)
        self.n += 1
        self.__swim(self.n - 1)

    def popmin(self):
        self.n -= 1
        self.__exchange(0, self.n)
        self.__sink(0)
        return self.pop()


R, N, T = map(int, input().split())
rockets = []
output = []
costs = [math.inf] * T

def compare_cost(pos, cost):
    if cost < costs[pos]:
        costs[pos] = cost
        heapq.heappush(path, (cost, pos))
        # path.heapadd((cost, pos))

for _ in range(R):
    rockets.append(tuple(map(int, input().split())))
path = []
# path = heap()
path.append((0, 0))
costs[0] = 0
while len(path) > 0:
    cur_cost, cur_pos = heapq.heappop(path)
    # cur_cost, cur_pos = path.popmin()
    if cur_cost != costs[cur_pos]:
        continue
    for c, f in rockets:
        pos = cur_pos + f
        cost = cur_cost + c
        if pos < T:
            compare_cost(pos, cost)
        pos = f - cur_pos
        if pos > 0:
            compare_cost(pos, cost)

for _ in range(N):
    output.append(costs[int(input())])
for line in output:
    print(line)

# for i in range(N):
#     path = heap()
#     visited = set()
#     path.heapadd((0, int(input())))
#     dequeued = path.popmin()
#     visited.add(cost)
#     while cost != 0:
#         for r in rockets:
#             position = abs(cost - r[1])
#             cost = pos + r[0]
#             if position in visited:
#                 old_node = [p[0] for p in path if p[1] == position]
#                 if len(old_node) > 0 and cost < old_node[0]:
#                     path.heapadd((cost, position))
#             else:
#                 path.heapadd((cost, position))
#             visited.add(position)
#         dequeued = path.popmin()
#     output.append(pos)

# for i in output:
#     print(i)