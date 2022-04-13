class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        DIR = [0, 1, 0, -1, 0]  # (r + DIR[i], c + DIR[i+1]) corresponding to move [RIGHT, DOWN, LEFT, TOP]
        r, c, d = 0, 0, 0
        for i in range(1, n*n+1):
            nr, nc = r + DIR[d], c + DIR[d+1]
            if not 0 <= nr < n or not 0 <= nc < n or ans[nr][nc] != 0:  # If out of bound or already visited
                d = (d + 1) % 4  # Change next direction
                nr, nc = r + DIR[d], c + DIR[d+1]
                
            ans[r][c] = i
            r, c = nr, nc
        
        return ans