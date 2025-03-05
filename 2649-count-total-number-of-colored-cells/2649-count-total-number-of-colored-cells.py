class Solution:
    def coloredCells(self, n: int) -> int: 
        return reduce(lambda a,x : a + 4 + (4 * (x - 2)), range(2,n + 1), 1)