class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = len(matrix) - 1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                row = i - 1
                break
        
        for val in matrix[row]:
            if val == target:
                return True
        
        return False
        

