class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l=len(nums)
        ans=0
        start=0
        end=0
        ct=0
        dct=defaultdict(int)
        while end<l:
            tmp=dct[nums[end]]
            ct+=tmp
            dct[nums[end]]+=1
            end+=1
            while ct>=k:
                ans+=l-end+1
                tmp=dct[nums[start]]
                ct-=tmp-1
                dct[nums[start]]-=1
                start+=1
        return ans       