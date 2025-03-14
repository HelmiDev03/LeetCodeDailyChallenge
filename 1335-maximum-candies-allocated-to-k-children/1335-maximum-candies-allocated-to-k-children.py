class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        l = 1
        r = max(candies)

        def check(nm):
            sm = 0
            for n in candies:
                sm += n // nm

            return sm 

        if check(1) < k:
            return 0

        
        while l <= r:

            mid = (l + r) // 2
        

            if check(mid) >= k:
                l = mid + 1
            else:
                r = mid - 1
       

        return r
        