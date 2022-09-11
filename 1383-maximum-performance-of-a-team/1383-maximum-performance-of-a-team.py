class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        h = []
        res = ssum = 0 
        for e,s in sorted(zip(efficiency, speed), reverse = 1):
            bisect.insort(h, -s)
            ssum += s
            if len(h) > k:
                ssum += h.pop()
            res = max(res, ssum*e)
            
        return res % (10**9 + 7)