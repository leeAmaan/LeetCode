class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove <= 0:
            return 0 
        
        mod = 10**9 + 7 
        count = [[0]*n for _ in range(m)]
        count[startRow][startColumn] = 1
        result = 0
        
        dirs =  [(-1,0),(1,0),(0,-1),(0,1)]
        
        for step in range(maxMove):
            temp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for d in dirs:
                        nr, nc = r + d[0], c + d[1]
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            result = (result + count[r][c]) % mod
                        else:
                            temp[nr][nc] = (temp[nr][nc] + count[r][c]) % mod
            count = temp

        return result