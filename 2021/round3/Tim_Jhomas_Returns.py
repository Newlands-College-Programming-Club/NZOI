# https://train.nzoi.org.nz/problems/1231

# N is the number of spies.
N, D = map(int, input().split())

class TallUnionTree:
    def __init__(self, n) -> None:
        self.id = []
        self.size = []
        for i in range(n):
            self.id.append(i)
            self.size.append(1)
    
    def root(self, i: int) -> int:
        while self.id[i] != i:
            i = self.id[i]
        return i
    
    def connected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)
    
    def union(self, p: int, q: int) -> None:
        i = self.root(p)
        j = self.root(p)
        if self.size[j] < self.size[i]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]