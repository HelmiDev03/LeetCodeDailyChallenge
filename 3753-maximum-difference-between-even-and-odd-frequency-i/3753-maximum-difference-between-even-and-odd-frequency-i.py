class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        d = Counter(s)

        odd = [v for v in d.values() if v % 2 == 1]
        even = [v for v in d.values() if v % 2 == 0]

        if not odd or not even:
            return -1

        ans = float('-inf')
        for i in odd:
            for j in even:
                ans = max(ans, i - j)

        return ans