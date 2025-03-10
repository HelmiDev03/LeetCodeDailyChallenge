class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (0 if word[i] in vowels else 1)
        
        last_occ = {v: -1 for v in vowels}
        
        freq = defaultdict(int)
        freq[prefix[0]] = 1  
        valid_ptr = 1 
        
        ans = 0
        for j in range(n):

            if word[j] in vowels:
                last_occ[word[j]] = j

            if any(last_occ[v] == -1 for v in vowels):
                continue

            m = min(last_occ.values())
            while valid_ptr <= m:
                freq[prefix[valid_ptr]] += 1
                valid_ptr += 1
            
            ans += freq[prefix[j+1] - k]
        
        return ans