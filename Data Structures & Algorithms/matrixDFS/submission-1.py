class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        directions = [[1,0] , [0,1] , [-1,0] ,[0,-1]]
        visit = set()
        def dfs(r , c , grid , visit , directions):
            R = len(grid)
            C = len(grid[0])
            if r<0 or c <0 or r>=R or c >=C or grid[r][c] == 1 or (r,c) in visit:
                return 0 
            if r == R -1 and c == C -1:
                return 1
            visit.add((r,c))
            count = 0
            for nr , nc in directions:
                result = dfs(r+nr,c+nc,grid,visit,directions)
                count += result
            visit.remove((r,c))
            return count
        count = dfs(0,0,grid,visit,directions)
        return count



        