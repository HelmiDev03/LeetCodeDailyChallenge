class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(axis = 0):
            rectangles.sort(key = lambda r: r[axis])
            cnt = 0
            start = rectangles[0][axis]
            end = rectangles[0][axis+2]
            for i in range(len(rectangles)):
                if rectangles[i][axis] < end:
                    if rectangles[i][axis+2] > end:
                        end = rectangles[i][axis+2]
                else:
                    cnt += 1
                    if cnt == 2:
                        return True
                    start, end = rectangles[i][axis], rectangles[i][axis+2]
            return False
        return check(axis=0) or check(axis=1)