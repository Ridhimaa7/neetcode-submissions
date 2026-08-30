class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        queue = deque()
        time = 0
        R = len(grid)
        C = len(grid[0])
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr,nc) < 0 or nr == R or nc == C or (nr,nc) in visited or grid[nr][nc] != 1:
                        continue
                    visited.add((nr,nc))
                    fresh_count -= 1
                    queue.append((nr,nc))
            time += 1
        if fresh_count:
            return -1
        else:
            return time