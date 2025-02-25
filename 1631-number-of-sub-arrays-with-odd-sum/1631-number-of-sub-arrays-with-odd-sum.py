class Solution:
    def __init__(self):
        self.modulo = (10 ** 9) + 7
    
    def numOfSubarrays(self, arr: List[int]) -> int:
        answer = 0
        element, oddCount, evenCount = 0, 0, 0
        for i in arr:
            element += i
            if element & 1:
                oddCount += 1
                answer += (evenCount + 1)
            else:
                evenCount += 1
                answer += oddCount

        return answer % self.modulo