class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)-1):
            if abs(points[i][0] - points[i+1][0]) > abs(points[i][1] - points[i+1][1]): 
                res += abs(points[i][0] - points[i+1][0])
            else: 
                res += abs(points[i][1] - points[i+1][1])
        return res 