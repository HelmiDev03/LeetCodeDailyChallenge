import itertools
import functools

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            for comb in itertools.combinations(nums, i):
                res += functools.reduce(lambda x, y: x ^ y, comb, 0)
                
        return res