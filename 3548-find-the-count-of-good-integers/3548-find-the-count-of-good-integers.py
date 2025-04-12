class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        # special case
        if n==1:
            cnt=0
            for i in range(1, 10):
                if i%k==0:
                    cnt+=1
            return cnt

        def gen_pali(n):
            

            start = 10**((n//2)-1) 
            end=start*10
            pali=[]
            if n%2==0:
                for i in range(start, end):
                    s=str(i)+str(i)[::-1]
                    pali.append(s)
            else:
                for i in range(start, end):
                    for middle in range(0,10):
                        s=str(i)+str(middle)+str(i)[::-1]
                        pali.append(s)
            return pali

        def make_k_pali(pali):
            ans=set()
            for p in pali:
                if int(p)%k==0:
                    ans.add(''.join(sorted(p)))
            return ans
        
        pali = gen_pali(n)

        def find_permutation(num):
            ans = math.factorial(n)
            num_counter = dict(Counter(num))

            for k,v in num_counter.items():
                if v>1:
                    ans=ans//math.factorial(v)

            if '0' in num_counter:
                temp=math.factorial(n-1)
                for k,v in num_counter.items():
                    if v>1:
                        if k=='0':
                            v-=1
                        temp=temp//math.factorial(v)
                ans=ans-temp
            return ans 
        pali_filtered = make_k_pali(pali)
        result=0
        for p in pali_filtered:
            result+=find_permutation(p)
        return result


            


        

            