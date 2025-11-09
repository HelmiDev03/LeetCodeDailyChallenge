class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def fct(x,y):
            if x == 0 or y == 0:
                return 0
            else:
                minn=min(x,y)
                maxx=max(x,y)
                return 1 + fct(minn, maxx-minn)  
        return fct(num1,num2)          
        