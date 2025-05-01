class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        def can_assign(n):
            task_i, temp, p = 0, deque(), pills
            for i in range(n - 1, -1, -1):
                while task_i < n and tasks[task_i] <= workers[i] + strength:
                    temp.append(tasks[task_i])
                    task_i += 1
                if not temp: return False
                if workers[i] >= temp[0]:
                    temp.popleft()
                elif p > 0:
                    temp.pop(); p -= 1
                else: return False
            return True

        tasks.sort()
        workers.sort(reverse=True)
        l, r, res = 0, min(len(tasks), len(workers)), 0
        while l <= r:
            m = (l + r) // 2
            if can_assign(m): res, l = m, m + 1
            else: r = m - 1
        return res