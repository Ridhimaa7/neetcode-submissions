class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        def dfs(r,c,visited):
            if r == R or c == C or min(r,c) < 0 or (r,c) in visited or grid[r][c] == 1:
                return 0
            if r == R - 1 and c == C - 1:
                return 1
            visited.add((r,c))
            count = 0
            count += dfs(r+1,c,visited)
            count += dfs(r-1,c,visited)
            count += dfs(r,c+1,visited)
            count += dfs(r,c-1,visited)
            visited.remove((r,c))
            return count
        return dfs(0,0,set())
        