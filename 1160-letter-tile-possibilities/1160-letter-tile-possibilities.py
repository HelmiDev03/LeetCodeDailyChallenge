class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        res = 0
        def dfs():
            nonlocal res
            for key in count:
                if count[key]:
                    res += 1
                    count[key] -= 1
                    dfs()
                    count[key] += 1
        dfs()
        return res