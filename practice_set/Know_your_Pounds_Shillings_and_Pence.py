N = int(input())
output = []

for case in range(N):

    s = int(input())
    total = [0, 0, 0]
    for _ in range(s):
        money = list(map(int, (input()[1:].split("-"))))
        total[0] += money[0]
        total[1] += money[1]
        total[2] += money[2]
    total[1] += total[2] // 12
    total[2] %= 12
    total[0] += total[1] // 20
    total[1] %= 20
    output.append("#{}-{}-{}".format(*total))

for i in output:
    print(i)