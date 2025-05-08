class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        minheap = [] 
        heappush(minheap, (0, 0, 0, 1))
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set([(0, 0)])
        while minheap:
            cost, r, c, s = heappop(minheap)
            if r == rows-1 and c == cols-1:
                return cost
            val = not s
            for row, col in dirs:
                dr = row + r
                dc = col + c
                if dr >= 0 and dc >= 0 and dr < rows and dc < cols and (dr, dc) not in visit:
                    new_cost = max(cost, moveTime[dr][dc]) + val + 1
                    visit.add((dr, dc))
                    heappush(minheap, (new_cost, dr, dc, val))

        return -1


        