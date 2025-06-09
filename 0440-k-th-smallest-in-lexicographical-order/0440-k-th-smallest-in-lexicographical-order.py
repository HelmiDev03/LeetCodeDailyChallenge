class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        curr = 1
        k -= 1  
        
        while k:
            
            count = 0
            first, last = curr, curr + 1
            
            
            while first <= n:
                count += min(n + 1, last) - first
                first *= 10
                last *= 10
            
            if k >= count:
               
                k -= count
                curr += 1
            else:
                
                curr *= 10
                k -= 1
                
        return curr