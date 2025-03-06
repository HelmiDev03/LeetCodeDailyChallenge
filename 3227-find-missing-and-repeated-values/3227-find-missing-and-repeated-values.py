class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)**2
        s = []
        for lis in grid:
            s += lis
        c = Counter(s)
        lisum = sum(s)
        t = (n * (n + 1)) // 2
        repeated = 0
        for key,val in c.items():
            if val == 2:
                repeated = key
        return [repeated, t - (lisum - repeated)]
