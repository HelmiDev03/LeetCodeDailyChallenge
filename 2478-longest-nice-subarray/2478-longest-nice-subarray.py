class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        left = 0
        right = 1
        maxLen = 1
        while right < len(nums):
            new = nums[right]
            for i in range(left, right):
                if (nums[i]&new) != 0:
                    left = i + 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
            