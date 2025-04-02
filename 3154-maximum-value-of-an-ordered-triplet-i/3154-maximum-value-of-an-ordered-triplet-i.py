class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        backwardmx = [nums[-1]] * len(nums)
        for i in range(len(nums)-2,-1,-1):
            backwardmx[i] = max(nums[i], backwardmx[i+1])

        forwardmx = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            forwardmx[i] = max(forwardmx[i-1], nums[i])

        ans = 0
        for i in range(1, len(nums)-1):
            ans = max(ans, (forwardmx[i-1] - nums[i]) * backwardmx[i+1])
                
        return ans