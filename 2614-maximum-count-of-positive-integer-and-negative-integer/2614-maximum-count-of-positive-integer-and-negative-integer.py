class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count = 0
        counts = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            elif nums[i] > 0:
                count += 1
            elif nums[i] < 0:
                counts += 1
        return max(count, counts)