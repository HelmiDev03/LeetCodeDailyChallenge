class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]
        visit1 = [-1] * n
        visit2 = [-1] * m

        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)

        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        def dfs(node, even, adj, visit):
            visit[node] = 0 if even else 1
            for nei in adj[node]:
                if visit[nei] == -1:
                    dfs(nei, not even, adj, visit)

        dfs(0, True, adj1, visit1)
        dfs(0, True, adj2, visit2)

        oddCount1 = sum(visit1)
        evenCount1 = n - oddCount1
        
        oddCount2 = sum(visit2)
        evenCount2 = m - oddCount2
        count2 = max(oddCount2, evenCount2)
        
        res = []
        for i in range(n):
            if visit1[i] == 1:
                res.append(oddCount1 + count2)
            else:
                res.append(evenCount1 + count2)
        return res