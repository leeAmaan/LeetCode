class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        for i in range(m//2):
            for j in range(m-m//2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j] 
        