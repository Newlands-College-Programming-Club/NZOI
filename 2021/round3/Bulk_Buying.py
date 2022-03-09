# https://train.nzoi.org.nz/problems/1232

N = int(input())
A = int(input())
B = int(input())

a = A / 2
b = B / 3
threes = 0
twos = 0

if a <= b:
    twos = N // 2
    remainder = N % 2
    if remainder:
        twos -= 1
        threes = 1
else:
    threes = N // 3
    remainder = N % 3
    if remainder == 1:
        threes -= 1
        twos = 2
    elif remainder == 2:
        twos = 1
print(A * twos + B * threes)