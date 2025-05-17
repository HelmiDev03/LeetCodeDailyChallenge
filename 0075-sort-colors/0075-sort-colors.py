class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, current, end = 0, 0, len(nums) - 1
        
        while current <= end:
            if nums[current] == 0:

                nums[start], nums[current] = nums[current], nums[start]
                start += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[end], nums[current] = nums[current], nums[end]
                end -= 1
        
        return nums  