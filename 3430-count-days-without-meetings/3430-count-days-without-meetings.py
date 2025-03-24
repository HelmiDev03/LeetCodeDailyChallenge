class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        #init
        meets = []
        for start, end in meetings:
            meets.append((start, end))

        meets = sorted(meets, key=lambda x: x[0])
        
        #algo
        totals = 0
        prevStart = 0
        prevEnd = 0
        for start, end in meets:
            if start > prevEnd: 
                totals += end - start + 1
                prevEnd = end
            elif end > prevEnd: 
                totals += end - prevEnd
                prevEnd = end

        return days - totals