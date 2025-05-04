class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = {x:{y:0 for y in range(1,x+1)} for x in range(1, 10)}
        pairs = 0
        for i,j in dominoes:
            if j>=i:
                i, j = j, i

            cnt[i][j] += 1
            pairs += (cnt[i][j] - 1)
        return pairs
        