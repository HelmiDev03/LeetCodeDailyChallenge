class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=[]
        for x in nums:
            if nums.count(x)>1 and x not in a :
                a.append(x)
        return a