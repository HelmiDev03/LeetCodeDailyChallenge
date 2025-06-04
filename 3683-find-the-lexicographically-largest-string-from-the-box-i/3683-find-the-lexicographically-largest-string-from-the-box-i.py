

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1: return word
        res = ""
        for i in range(n):
            res = max(res , word[i : min(i+n-numFriends+1 , n)])
        return res