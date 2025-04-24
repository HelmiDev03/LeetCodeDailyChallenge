class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_nums = sorted(list(set(nums)))
        left = 0
        right = 0
        total_count = 0
        while right < len(nums):
            sub_array = nums[left:right+1]
            if sorted(list(set(sub_array))) == distinct_nums:
                    total_count += len(nums) - right
                    print(total_count)
                    right = left
                    left += 1
            right+=1
        return total_count