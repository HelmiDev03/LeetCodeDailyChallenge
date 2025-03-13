class Solution:
    def minZeroArray(self, nums: List[int], q: List[List[int]]) -> int:
        n = len(nums)
        if sum(nums)==0:
            return 0
        def makeArrayZero(k):
            diff = [0]*(n+1)
            for i in range(k):
                left,right,val=q[i]
                diff[left]+=val
                diff[right+1]-=val
            curr = 0
            print(diff)
            for index,i in enumerate(nums):
                curr += diff[index]
                print(curr, i )
                if curr<i:
                    return False
            return True
        left = 0 
        right = len(q)
        if not makeArrayZero(right):
            return -1
        while left < right:
            mid = (left + right)//2
            if makeArrayZero(mid):
                right = mid 
            else:
                left = mid + 1
        return left
            

            

        