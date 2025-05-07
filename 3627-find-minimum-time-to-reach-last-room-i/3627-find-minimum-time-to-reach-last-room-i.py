class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        n,m = len(moveTime),len(moveTime[0])
        for i in moveTime:
            print(i)

        q = []
        heappush(q,[0,0,0])
        vis = set()
        vis.add((0,0))
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        res = float('inf')
        while q:
            c,a,b = heappop(q)
            if a==n-1 and b==m-1:
                res = min(c,res)
                continue

            for x,y in dire:
                i,j = a+x,b+y
                if -1<i<n and -1<j<m and (i,j) not in vis:
                    vis.add((i,j))
                    heappush(q,[c+max(0,moveTime[i][j]-c)+1,i,j])
        return res
        