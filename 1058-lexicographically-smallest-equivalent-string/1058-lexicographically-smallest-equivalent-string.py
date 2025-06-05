class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False 

        if root_x < root_y:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
        return True


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        l = len(s1)
        for i in range(l):
            uf.union(ord(s1[i]) - 97, ord(s2[i]) - 97)
        ans = ''
        for i in baseStr:
            ans += chr(uf.find(ord(i) - 97) + 97)
        return ans
        
        