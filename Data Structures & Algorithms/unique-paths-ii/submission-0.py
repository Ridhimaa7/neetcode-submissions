class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dp(r,c,cache):
            if r == R or c == C or obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == R -1 and c == C - 1:
                return 1
            cache[r][c] = dp(r+1,c,cache) + dp(r,c+1,cache)
            return cache[r][c]
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])
        cache = [[0] * C for _ in range(R)]
        if obstacleGrid[0][0] == 1:
            return 0
        return dp(0,0,cache)
        