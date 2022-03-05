class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            if merged == []:
                merged.append(intervals[i])
            else:
                if intervals[i][0] <= merged[-1][1]: # overlap
                    merged[-1][1] = max(merged[-1][1],intervals[i][1])
                else:
                    merged.append(intervals[i])
        return merged