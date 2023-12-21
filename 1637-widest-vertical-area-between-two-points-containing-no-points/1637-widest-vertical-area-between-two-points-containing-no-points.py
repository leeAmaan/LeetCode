class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = []
        maxi = 0

        for point in points:
            ans.append(point[0])

        ans.sort()

        for i in range(len(ans) - 1, 0, -1):
            maxi = max(maxi, ans[i] - ans[i-1])

        return maxi
