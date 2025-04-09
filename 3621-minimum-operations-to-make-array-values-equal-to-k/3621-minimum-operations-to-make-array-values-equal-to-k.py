class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return (lambda x: len(set(nums)) - (k == x) if k <= x else -1)(min(nums))