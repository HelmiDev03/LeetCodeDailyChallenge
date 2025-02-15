class Solution:
    def punishmentNumber(self, n: int) -> int:
        def helper(to_split, target):
            l = len(str(to_split))
            if l == 1:
                return to_split == target
            for i in range(l - 1, -1, -1):
                a, b = divmod(to_split, 10**i)
                if a > target:
                    break
                if helper(b, target - a):
                    return True
            return False

        return sum(sq for num in range(1, n + 1) if (sq := num**2) and helper(sq, num))