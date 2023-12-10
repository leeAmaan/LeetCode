import numpy as np 

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans_matrix = np.zeros([len(matrix[0]), len(matrix)], dtype = np.int32)
        # [[0,0,0],[0,0,0],[0,0,0]]
        for j in range(len(matrix)):
            for i in range(len(matrix[0])):
                trans_matrix[i][j] = matrix[j][i]
        return trans_matrix