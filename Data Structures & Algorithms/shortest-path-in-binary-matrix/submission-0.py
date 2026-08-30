class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque()
        R = len(grid)
        C = len(grid[0])
        queue.append((0,0))
        visited = set([(0,0)])
        length = 1
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if r == R -1 and c == C - 1:
                    return length
                directions = [[0,1],[0,-1], [1,0], [-1,0],[1,1],[-1,1],[-1,-1],[1,-1]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr,nc) in visited or min(nr,nc) < 0 or nr == R or nc == C or grid[nr][nc] == 1:
                        continue
                    visited.add((nr,nc))
                    queue.append((nr,nc))
            length += 1
        return -1