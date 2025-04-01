class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1] * n
        
        def dfs(q_idx):
            if q_idx >= n:
                return 0
            
            if dp[q_idx] != -1:
                return dp[q_idx]
            
            pts = questions[q_idx][0]
            skip = questions[q_idx][1]

            dp[q_idx] = max(pts+dfs(q_idx+skip+1), dfs(q_idx+1))

            return dp[q_idx]
        
        dfs(0)
        return dp[0]