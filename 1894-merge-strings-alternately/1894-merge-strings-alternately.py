class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        times = min(len(word1), len(word2))
        ans = ''
        for i in range(times):
            ans += (word1[i] + word2[i])
        ans += word1[times:] + word2[times:]
        return ans