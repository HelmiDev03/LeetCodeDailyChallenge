class Solution:
    def clearStars(self, s: str) -> str:
        result = [True] * len(s)
        heap = []
        for i, ch in enumerate(s):
            if ch != "*":
                heapq.heappush(heap, (ch, -i))
            else:
                result[i] = False
                if heap:
                    _, index = heapq.heappop(heap)
                    result[-index] = False
        
        ans = ""
        for i in range(len(s)):
            if result[i]:
                ans += s[i]
        return ans
