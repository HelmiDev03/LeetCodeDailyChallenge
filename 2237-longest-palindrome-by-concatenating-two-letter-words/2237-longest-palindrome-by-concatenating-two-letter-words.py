class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        Equal = {}

        for i in words:
            if i[0] == i[1]:
                if i in Equal:
                    Equal[i] += 1
                else:
                    Equal[i] = 1
            
            else:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        

        taken = set()
        ans = 0
        
        for i in d.keys():
            f , s = i[0] , i[1]

            if (s+f in d) and (i not in taken) and (s+f not in taken):
                ans += min(d[i] , d[s+f]) * 4
                taken.add(i)
                taken.add(f+s)
            
        odd = False

        for i in Equal.keys():
            if Equal[i]%2 == 0:
                ans += Equal[i] * 2

            else:
                if Equal[i] == 1:
                    odd = True
                
                else:
                    ans += (Equal[i] - 1) * 2
                    odd = True
                
        
        if odd:
            ans += 2

        return ans