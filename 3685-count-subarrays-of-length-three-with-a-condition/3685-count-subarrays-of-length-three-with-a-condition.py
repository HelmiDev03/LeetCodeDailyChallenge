class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        sz = len(nums)
        i = 0
        cnt = 0
        for i in range (sz-2):
            if (nums[i] + nums[i+2]) == (nums[i+1] * 0.5):
                cnt+=1 
            
        return cnt