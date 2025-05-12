class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def fn(nums):
            c=1
            s=0
            for i in reversed(nums):
                s += i*c
                c*=10
            return s
        c=permutations(digits, 3)
        ll=set()
        for i in c:
            if i[-1]%2!=0 or i[0]==0: continue
            s=fn(i)
            ll.add(s)
        x=list(ll)
        x.sort()
        return x