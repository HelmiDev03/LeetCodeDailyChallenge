class Solution:
    def compress(self, s):
        count = 0
        current = s[0]
        res = ""
        for c in s:
            if c == current:
                count += 1
            else:
                res += str(count) + current
                count = 1
                current = c
        res += str(count) + current
        return res

    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(n - 1):
            s = self.compress(s)
            print(s)
        return s


