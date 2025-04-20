class Solution:
    def numRabbits(self, answers):
        count = Counter(answers)
        res = 0
        for x in count:
            group_size = x + 1
            groups_needed = math.ceil(count[x] / group_size)
            res += groups_needed * group_size
        return res