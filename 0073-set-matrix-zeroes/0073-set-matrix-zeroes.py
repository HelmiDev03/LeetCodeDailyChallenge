class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        row = set()
        col = set()

        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 0:
                    row.add(i)
                    col.add(j)
                    
        for i in row:
            m[i] = [0] * len(m[i])

        for i in range(len(m)):
            for j in col:
                m[i][j] = 0
        
        