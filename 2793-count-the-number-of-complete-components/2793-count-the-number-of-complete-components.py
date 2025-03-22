class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        degree = [0] * n
        
        
        for a, b in edges:
            if dsu.find(a) != dsu.find(b):
                dsu.union(a, b)
            degree[a] += 1
            degree[b] += 1
        
       
        components = {}
        for i in range(n):
            root = dsu.find(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
        
        ans = 0
       
        for comp_nodes in components.values():
         
            if len(comp_nodes) <= 2:
                ans += 1
                continue
            complete = True
        
            for node in comp_nodes:
                if degree[node] != len(comp_nodes) - 1:
                    complete = False
                    break
            if complete:
                ans += 1
        return ans