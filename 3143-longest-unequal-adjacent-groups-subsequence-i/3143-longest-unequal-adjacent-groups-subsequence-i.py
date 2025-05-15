class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if len(words)==1:
            return words
        if 0 not in groups or 1 not in groups:
            return [words[0]]
        s=[words[0]]
        for i in range(1,len(words)):
            if(groups[i-1]!=groups[i]):
                s.append(words[i])
        return s