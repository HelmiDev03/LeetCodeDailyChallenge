class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        nums = weights
        n = len(nums)
        maxheap = [-1*(nums[i] + nums[i+1]) for i in range(n-1)]
        heapq.heapify(maxheap)
        minheap = [(nums[i] + nums[i+1]) for i in range(n-1)]
        heapq.heapify(minheap)

        m = 0
        M = 0

        for _ in range(k-1):

            M += -1*heapq.heappop(maxheap)
            m += heapq.heappop(minheap)

        return M-m