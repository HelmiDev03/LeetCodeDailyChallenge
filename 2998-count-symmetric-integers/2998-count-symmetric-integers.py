class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def is_symmetric(n):
            num = str(n)
            if len(num) % 2 != 0:
                return False
            
            s1, s2 = 0, 0
            i, j = 0, len(num) // 2
            while j < len(num):
                s1 += int(num[i])
                s2 += int(num[j])
                i += 1
                j += 1
            return s1 == s2

        res = 0
        for n in range(low, high + 1):
            if is_symmetric(n):
                res += 1
        return res