
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        adj = [[num] for num in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(adj[j]) + 1 > len(adj[i]):
                    adj[i] = adj[j] + [nums[i]]

        return max(adj, key = len)