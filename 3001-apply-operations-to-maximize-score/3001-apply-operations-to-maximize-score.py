MOD = int(1e9) + 7
MAX_NUM = int(1e5)

not_prime = list(range(MAX_NUM + 1))
for i in range(2, int(MAX_NUM**0.5) + 1):
    if not_prime[i] != i:
        continue
    for j in range(i * i, MAX_NUM + 1, i):
        if not_prime[j] == j:
            not_prime[j] = i

prime_score = [0] * (MAX_NUM + 1)
for i in range(2, len(prime_score)):
    n = i
    factors = set()
    while n != 1:
        factors.add(not_prime[n])
        n //= not_prime[n]
    prime_score[i] = len(factors)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        prime_score_num = [prime_score[x] for x in nums]

        prime_score_num.append(MAX_NUM)
        stack = []
        freq = Counter()
        for end in range(len(prime_score_num)):
            while stack and prime_score_num[stack[-1]] < prime_score_num[end]:
                i = stack.pop()
                beg = stack[-1] if stack else -1
                freq[nums[i]] += (i - beg) * (end - i)
            stack.append(end)


        total_score = 1        
        for score in sorted(freq, reverse=True):
            ops = min(k, freq[score])
            total_score = (total_score * pow(score, ops, MOD)) % MOD
            k -= ops
            if k == 0:
                break

        return total_score
        