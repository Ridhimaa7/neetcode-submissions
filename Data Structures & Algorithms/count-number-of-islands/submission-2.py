class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        def dfs(r,c,visited):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or (r,c) in visited or grid[r][c] == "0":
                return
            visited.add((r,c))
            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)


        for R in range(len(grid)):
            for C in range(len(grid[0])):
                if grid[R][C] == "1" and (R,C) not in visited:
                    res += 1
                    dfs(R,C,visited)
        return res