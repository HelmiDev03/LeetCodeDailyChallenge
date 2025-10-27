class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        a = []
        for x in bank:
            s = sum(int(ch) for ch in x)
            if s != 0:
                a.append(s)
        if len(a)<2:
            return 0
        s=0
        for i in range(len(a)-1):
            s+=a[i]*a[i+1]            


        return s
        