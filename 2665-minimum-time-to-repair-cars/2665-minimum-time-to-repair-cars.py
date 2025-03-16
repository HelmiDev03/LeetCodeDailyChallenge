class Solution:
    def repairCars(self, r: List[int], c: int) -> int:
        l, m = 0, min(r) * c * c
        while l < m:
            t = (l + m) // 2
            s = sum(int(math.sqrt(t // i)) for i in r)
            if s >= c:
                m = t
            else:
                l = t + 1
        return l