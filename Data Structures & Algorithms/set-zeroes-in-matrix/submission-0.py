class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_cols = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0

