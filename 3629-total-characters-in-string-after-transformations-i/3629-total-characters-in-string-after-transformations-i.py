class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = deque([0] * 26)
        counter = Counter(s)
        
        for x in counter:
            freq[ord(x) - 97] = counter[x]

        for _ in range(t):
            z = freq.pop()
            freq.appendleft(z)
            freq[1] = (freq[1] + z) % (10**9 + 7)
        
        return sum(freq) % (10**9 + 7)