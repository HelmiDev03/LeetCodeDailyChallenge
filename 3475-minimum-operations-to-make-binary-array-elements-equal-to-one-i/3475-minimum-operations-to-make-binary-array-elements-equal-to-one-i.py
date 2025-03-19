class Solution:
    def minOperations(self, nums: List[int]) -> int:
        times = 0
        i = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1  
                nums[i + 2] ^= 1
                times += 1
        return times if nums[i + 1] == 1 and nums[i + 2] == 1 else -1