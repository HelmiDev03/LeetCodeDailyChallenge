class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = len(min(strs, key=len))
        sghir = 1
        high = min_len
        while sghir <= high:
            mid = (sghir + high)//2
            prefix = strs[0][:mid]
            if all(s.startswith(prefix) for s in strs[1:]):
                sghir = mid + 1
            else:
                high = mid - 1
        return strs[0][:(sghir + high)//2]