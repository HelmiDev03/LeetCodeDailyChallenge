class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def f(x):
            cnt = []
            for i, n in enumerate(nums):
                if n <= x and ((cnt and i - cnt[-1][0] > 1) or not cnt):
                    cnt.append((i, n))
            return len(cnt) >= k
        left = min(nums)-1
        right = max(nums) + 1
        while left+1 < right:
            mid = (left+right) // 2
            if f(mid):
                right = mid
            else:
                left = mid
        return right
            