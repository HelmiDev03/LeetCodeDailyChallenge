class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        md = (10 ** 9) + 7
        prev = deque([1, 1])
        tot = 0
        for i in range(2, n + 1):
            val = (sum(prev) + 2 * (tot)) % md 
            tot += prev.popleft()
            prev.append(val)
        return val


        