class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        list1 = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count = count + self.dfs(grid , i , j)
                    list1.append(count)
        return len(list1)
    def dfs(self , grid , r , c):
        R = len(grid)
        C = len(grid[0])
        if r>=R or c>=C or r<0 or c<0 or grid[r][c] == '0' :
            return 0 
        else:
            grid[r][c] = '0'
            return 1 + self.dfs(grid , r + 1 , c) + self.dfs(grid , r - 1 ,c)+ self.dfs(grid , r , c - 1)+ self.dfs(grid , r , c + 1)