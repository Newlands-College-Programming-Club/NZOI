# https://train.nzoi.org.nz/problems/1228

SHOES = input()

reds = SHOES.count("R")

if reds == 2:
    print("Dorothy is in the classroom.")
elif reds == 1:
    print("Hop along Dorothy and find that other shoe.")
else:
    print("Maybe Dorothy is in Kansas.")