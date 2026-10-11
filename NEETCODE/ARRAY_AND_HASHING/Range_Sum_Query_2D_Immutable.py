class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return
        
        ROWS, COLS = len(matrix), len(matrix[0])
        # Khởi tạo mảng prefix sum thêm 1 hàng và 1 cột chứa số 0
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Điền giá trị vào bảng prefix
        for r in range(ROWS):
            for c in range(COLS):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix[r][c + 1]
                    + self.prefix[r + 1][c]
                    - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Áp dụng công thức Bao hàm - Loại trừ
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )