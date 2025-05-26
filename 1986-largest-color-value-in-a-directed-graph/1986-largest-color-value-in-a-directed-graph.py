
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        
        count = [[0] * 26 for _ in range(n)]
        
        
        q = deque([i for i in range(n) if indegree[i] == 0])
        
        visited = 0
        res = 0
        
        while q:
            node = q.popleft()
            visited += 1
            color_index = ord(colors[node]) - ord('a')
            count[node][color_index] += 1
            res = max(res, count[node][color_index])
            
            for nei in graph[node]:
                for i in range(26):
                    count[nei][i] = max(count[nei][i], count[node][i])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if visited == n else -1