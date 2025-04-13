class Solution:
    def countGoodNumbers(self, n: int) -> int:

        x=5
        y=4
        mo=(10**9)+7
        def exp_multi(pow,base):
            result=1

            while pow>0:
                if pow%2==1:
                    result=(result*base)%mo
                base=(base*base)%mo
                pow//=2
            return result%mo
        return exp_multi(((n+1)//2),5)*exp_multi(n//2,4) %mo





        