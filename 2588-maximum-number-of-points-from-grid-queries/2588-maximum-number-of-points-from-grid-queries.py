class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])  
        queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])  
        res = [0] * len(queries)  
        
        heap = [(grid[0][0], 0, 0)]  
        visited = set()  
        visited.add((0, 0))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        points = 0  
        
        for i, query in queries_sorted:
            while heap and heap[0][0] < query:  
                val, r, c = heappop(heap)  
                points += 1  
                
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc  
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        heappush(heap, (grid[nr][nc], nr, nc))  
                        visited.add((nr, nc))  
            
            res[i] = points  
        
        return res