import collections
import heapq



class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        lookup = collections.defaultdict(list)
        for idx, (st, pt) in enumerate(tasks):
            lookup[st].append((pt, idx, st))
        heap, ans, last = [], [], 0
        for t in sorted(lookup):
            while heap and last < t:
                pt, idx, st = heapq.heappop(heap)
                last = max(st, last) + pt
                ans.append(idx)
            for pt, idx, st in lookup[t]:
                heapq.heappush(heap, (pt, idx, st))
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans
        