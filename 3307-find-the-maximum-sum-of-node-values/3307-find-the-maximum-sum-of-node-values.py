class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        #differences between a value x and it's xor value with k
        #sorted from largest to smallest
        xor_diffs = sorted([(x^k) - x for x in nums], reverse = True) 
        
        total = sum(nums)

        #iterate through pairs of xor_diffs
        for i in range(1,len(nums),2):
            #if we find a pair that is net negative, we are done
            if xor_diffs[i-1] + xor_diffs[i] < 0:
                break
            
            #add each useful pair   
            total += xor_diffs[i-1] + xor_diffs[i]

        return total