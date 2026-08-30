class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        number = 0
        def dfs(r,c):
            if min(r,c) < 0 or r >= len(grid) or c >= len(grid[0]) or (r,c) in visited or grid[r][c] == "0":
                return
            visited.add((r,c))
            dfs(r + 1 , c)
            dfs(r - 1 , c)
            dfs(r , c + 1)
            dfs(r , c - 1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != "0" and (r,c) not in visited:
                    dfs(r,c)
                    number += 1
        return number