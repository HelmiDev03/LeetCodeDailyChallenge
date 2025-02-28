class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0 
        j = 0 

        while i < n:
            while i < n and nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            i += 1

            


        
        


        