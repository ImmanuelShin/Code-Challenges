class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])

        no_row = [False] * m
        no_column = [False] * n

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    no_row[row] = True
                    no_column[col] = True
        
        for row in range(m):
            for col in range(n):
                if no_row[row] or no_column[col]:
                    matrix[row][col] = 0