class Solution:
    def maximum69Number (self, num: int) -> int:
        for i in range(len(str(num))):
            if str(num)[i]=='6':
                a=list(str(num))
                a[i]='9'
                return int("".join(a))
        return num        

        