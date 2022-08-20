class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        priorityQ = []
        ans, i = 0, 0
        while startFuel < target:
            while i < len(stations) and stations[i][0] <= startFuel:
                heapq.heappush(priorityQ,-stations[i][1])
                i += 1
            if not priorityQ:
                return -1
            startFuel += -heapq.heappop(priorityQ)
            ans += 1
        return ans