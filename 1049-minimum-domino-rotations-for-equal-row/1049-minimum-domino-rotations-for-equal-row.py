class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        t,b = defaultdict(int) , defaultdict(int)
        ans = []
        for i in range(n):
            t[tops[i]]+= 1
            b[bottoms[i]]+= 1
        
        majrty_in_t , majrty_in_b = set() ,set()
        txfreq , bxfreq = max(t.values()) , max(b.values())


        for i in range(n):
            if  t[tops[i]] == txfreq :
                 majrty_in_t.add(tops[i])

            if  b[bottoms[i]] == bxfreq :
                 majrty_in_b.add(bottoms[i])
       
        ans = []

        for x in t:
            temp= set()
            unique_count  = 0
            if t[x] >= n//2:

                for i,j in enumerate(tops):
                    if x == j:
                        temp.add(i)
                
                for i,j in enumerate(bottoms):
                    if x == j:
                        if i not in temp:
                            temp.add(i)
                            unique_count+= 1
            
            if len(temp) == n:
                ans.append(unique_count)
    
        for x in b:
            temp= set()
            unique_count  = 0
            if b[x] >= n//2:

                for i,j in enumerate(bottoms):
                    if x == j:
                        temp.add(i)
                
                for i,j in enumerate(tops):
                    if x == j:
                        if i not in temp:
                            temp.add(i)
                            unique_count+= 1
            
            if len(temp) == n:
                ans.append(unique_count)
        
        
        if len(ans):
            ans.sort()
            return ans[0]
        
        return -1