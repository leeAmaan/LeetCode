# import numpy as np 

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # trans_matrix = np.zeros([len(matrix[0]), len(matrix)], dtype = np.int32)
        ans=[[0]*len(matrix) for _ in range((len(matrix[0])))]
        for j in range(len(matrix)):
            for i in range(len(matrix[0])):
                ans[i][j] = matrix[j][i]
        return ans