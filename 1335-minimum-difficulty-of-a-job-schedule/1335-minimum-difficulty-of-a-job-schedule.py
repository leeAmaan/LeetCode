import functools

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jDL = len(jobDifficulty)
        if jDL < d:
            return -1 
        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            res, maxD = float('inf'), 0
            for j in range(i, jDL - d + 1):
                maxD = max(maxD, jobDifficulty[j])
                res = min(res, maxD + dfs(j + 1, d - 1))
            return res
        return dfs(0,d)