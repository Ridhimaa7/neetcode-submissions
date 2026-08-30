class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(matrix , r , c , values):
            R = len(matrix)
            C = len(matrix[0])
            if min(r,c) < 0 or r >= R or c >= C or matrix[r][c] == 1 or (r,c) in values:
                return 0
            elif r == R - 1 and c == C - 1 :
                #values.remove((r,c))
                return 1
            values.add((r,c))
            count = 0
            count += dfs(matrix , r+1 , c , values)
            count += dfs(matrix , r - 1 , c , values)
            count += dfs(matrix , r , c+1 , values)
            count += dfs(matrix , r , c - 1 , values)
            values.remove((r,c))
            return count
        values = set()
        return dfs(grid , 0 , 0 , values)
        