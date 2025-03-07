class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        sieveArray = [True]*(right+1)

     
        sieveArray[0] = sieveArray[1] = False
        
        prev, diff = -1, float('inf')
        res = [-1, -1]

   
        for i in range(2, int(right**0.5)+1):
            if sieveArray[i]:
                for j in range(i*i, right+1, i):
                    sieveArray[j] = False

        for i in range(left, right+1):
            if sieveArray[i]:
                if prev != -1 and i - prev < diff:
                    res = [prev, i]
                    diff = i - prev
                prev = i
        return res