# https://train.nzoi.org.nz/problems/1204

N = int(input())
number_values = list(map(int, input().split()))
A, M, E = map(int, input().split())

def cost(n):
    return sum(map(lambda x: number_values[int(x)], str(n)))

best = cost(N)

for i in range(1, N + 1):
    current = cost(i)
    # Check for cheaper alternatives of i
    j = 1
    while j * j <= i:
        if i % j == 0:
            current = min(current, cost(i // j) + cost(j) + M)
        j += 1
    if i < N:
            current += cost(N - i) + A
    best = min(best, current)

print(best + E)