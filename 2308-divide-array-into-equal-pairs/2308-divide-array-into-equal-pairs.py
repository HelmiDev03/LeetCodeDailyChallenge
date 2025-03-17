class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = [0]*501
        for i in nums:
            freq[i]+=1
        for i in freq:
            if i%2!=0:
                return False
        return True