class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        d = dict()
        for i in range(len(arr)):
            d[arr[i]] = i
        
        candidates = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                local_sum = arr[i] + arr[j]
                if local_sum in d and d[local_sum] > j:
                    candidates.append((i, j))
        
        res = 0
        for candidate in candidates:
            current_len = 2
            f, s = candidate[0], candidate[1]
            if len(arr) - f < res:
                break
            while True:
                if arr[f] + arr[s] in d:
                    f, s = s, d[arr[f] + arr[s]]
                    current_len += 1
                else:
                    res = max(res, current_len)
                    break

        return res