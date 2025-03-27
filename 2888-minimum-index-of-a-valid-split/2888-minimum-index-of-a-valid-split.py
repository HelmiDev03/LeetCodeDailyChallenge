class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d=Counter()
        d2=Counter(nums)

        n=len(nums)
       
        for i in range(n):
            d[nums[i]]+=1
            d2[nums[i]]-=1
           
            if d[nums[i]]> ((i+1)-d[nums[i]]) and d2[nums[i]]> (n-(i+1))-d2[nums[i]]: return i 

        return  -1