
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        deltaArray = [0] * (len(nums) + 1)

        for left, right in queries:
            deltaArray[left] += 1
            deltaArray[right + 1] -= 1
        
        current = 0
        for i in range(len(nums)):
            current += deltaArray[i]
            if current < nums[i]:
                return False
        return True