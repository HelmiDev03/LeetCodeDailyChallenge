class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m=len(grid)
        n=len(grid[0])
        rem=grid[0][0]%x
        lista=[]
        for i in range(m):
            for j in range(n):
                lista.append(grid[i][j])
                if rem!=grid[i][j]%x:
                    return -1
        lista.sort()
        k= m*n //2
        target=lista[k]
        moves=0
        for i in range(m*n):
            moves+=(abs(lista[i]-target)//x)
        return moves

        