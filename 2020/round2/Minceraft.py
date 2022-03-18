# https://train.nzoi.org.nz/problems/1167

M, R = map(int, input().split())
minces = list(map(int, input().split()))
required = [0] * (M + 1)
rafts = dict()
rafts = dict((m, 1) for m in range(1, M + 1))
for r in range(M + 1, M + R + 1):
    line = list(map(int, input().split()))
    rafts[r] = dict(((line[i], line[i + 1]) for i in range(1, line[0] * 2, 2)))

def find_material(mince, quantity):
    if rafts[mince] == 1:
        required[mince] += quantity
        return
    for m, q in rafts[mince].items():
        find_material(m, quantity * q)

def calculate():
    find_material(R + M, 1)
    return min(minces[i - 1] // required[i] for i in range(1, M + 1) if required[i] != 0)

print(calculate())