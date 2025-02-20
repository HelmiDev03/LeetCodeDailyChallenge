class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        s = set()
        x = len(nums[0])
        minx = "0" * x

        for elem in nums:
            s.add(elem)
            if elem == minx:
                while minx in s:
                    temp = int(minx, 10)
                    temp += 1
                    minx = bin(temp)[2:]
                    while len(minx) < x:
                        minx = "0" + minx
        return minx