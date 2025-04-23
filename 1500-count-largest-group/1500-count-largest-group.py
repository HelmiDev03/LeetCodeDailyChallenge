class Solution:
    def calcSum(self,k):
            k=str(k)
            ret=0
            for i in k:
                ret+=int(i)
            return ret
    def countLargestGroup(self, n: int) -> int:
        myHash=defaultdict(list)
        for i in range(1,n+1):
            x=self.calcSum(i)
            myHash[x].append(i)
        myLen=defaultdict(int)
        for i,v in myHash.items():
            myLen[len(v)]+=1
        print(myLen)
        return myLen[max(myLen)]