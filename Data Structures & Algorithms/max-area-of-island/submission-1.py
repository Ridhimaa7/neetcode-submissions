class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C or (r,c) in visited or grid[r][c] == 0:
                return 0
            sumarea = 1
            visited.add((r,c))
            sumarea += dfs(r + 1 , c)
            sumarea += dfs(r - 1, c)
            sumarea += dfs(r, c + 1)
            sumarea += dfs(r , c - 1)
            return sumarea
        R = len(grid)
        C = len(grid[0])
        for r in range(0,R):
            for c in range(0,C):
                if (r,c) not in visited and grid[r][c]!= 0:
                    maxArea = max(maxArea , dfs(r,c))
        return maxArea