class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        q = deque()
        first_k = 0
        rs = 0
    
        for i in range(len(nums)):
            if nums[i] == max_num:
                q.append(i)
            if len(q) > k:
                q.popleft()
            if len(q) == k:
                first_k = q[0]
                rs += first_k + 1
        return rs
                