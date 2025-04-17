class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        
        res = 0
        hm = {}

        for index, num in enumerate(nums):
            if num in hm:
                for idx in hm[num]:
                    if (idx*index)%k ==0:
                        res +=1
                
                hm[num].append(index)
            
            else:
                hm[num] = [index]
        
        return res
        