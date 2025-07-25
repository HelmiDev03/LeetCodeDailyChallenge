class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sub = set()
        mx_sum = 0
        for i in nums:

            
            if i not in sub and i>=0:
                mx_sum +=i
                sub.add(i) 

        
        return mx_sum if sub else max(nums) 