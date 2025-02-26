class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = max_sum = min_sum = 0
        
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum)
            min_sum = min(min_sum, prefix_sum)
        
        return abs(max_sum - min_sum)