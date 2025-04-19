from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            
            left = lower - nums[i]
            right = upper - nums[i]

            
            left_idx = bisect_left(nums, left, i + 1, n)
            right_idx = bisect_right(nums, right, i + 1, n)

            count += (right_idx - left_idx)

        return count