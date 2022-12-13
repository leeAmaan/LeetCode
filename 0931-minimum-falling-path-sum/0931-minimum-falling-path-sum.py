class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        for i in range(1, len(m)):
            for j in range(len(m[0])):
                
                if j == 0:
                    m[i][j] = min((m[i][j] + m[i-1][j]), (m[i][j] + m[i-1][j+1]))
                elif (j == len(m[0]) - 1):
                    m[i][j] = min((m[i][j]+m[i-1][j]), (m[i][j] + m[i-1][j-1]))
                else:
                    m[i][j] = min(m[i][j] + m[i-1][j], m[i][j] + m[i-1][j+1], m[i][j] + m[i-1][j-1])
                    
        return min(m[len(m)-1])
        
        
        #n = len(matrix[0])
        #ans = 0
        #for i in range(n):
        #    #matrix[i]
        #    li = []
        #    for j in range(n): 
        #        li.append(matrix[i][j])
        #        print(li)
        #    ans += min(li)
        #    print(ans)
        #return ans