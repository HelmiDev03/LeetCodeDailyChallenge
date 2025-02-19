class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        for p in product('abc', repeat=n):
            s = ''.join(p)
            if not search(r'(.)\1', s):
                k -= 1
                if k == 0:
                    return s
        return ''