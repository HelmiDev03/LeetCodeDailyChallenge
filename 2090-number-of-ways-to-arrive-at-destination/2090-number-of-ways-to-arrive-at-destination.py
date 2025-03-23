

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = int(1e9) + 7
        d = defaultdict(list)

        for u, v, time in roads:
            d[u].append([v, time])
            d[v].append([u, time])

        min_time = [float("inf")] * n
        min_time[0] = 0
        ways = [0] * n
        ways[0] = 1

        heap = [(0, 0)]  # Min-heap (time, node)

        while heap:
            time, node = heappop(heap)

            if time > min_time[node]:
                continue

            for neighbor, travel_time in d[node]:
                new_time = time + travel_time

                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heappush(heap, (new_time, neighbor))
                elif new_time == min_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % mod

        return ways[n - 1]  