class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        res = i = 0 
        while startFuel < target:
            while i < len(stations) and stations[i][0] <= startFuel:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq:
                return -1 
            startFuel += -heapq.heappop(pq)
            res += 1
        return res