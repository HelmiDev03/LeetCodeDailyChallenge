class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def C(n):
            if n < 0:
                return 0
            else:
                return (n + 2) * (n + 1) // 2
        return ( C(n) 
                - 3 * C(n - limit - 1)
                + 3 * C(n - 2 * (limit + 1))
                - C(n - 3 * (limit + 1))
        )