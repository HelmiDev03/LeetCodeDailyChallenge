class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        t = 0
        l = 0
        c = 0
        for r in range(n):
            c+= nums[r]

            while l <= r and c * (r - l + 1) >= k:
                c -= nums[l]
                l += 1

            t += (r - l + 1)

        return t