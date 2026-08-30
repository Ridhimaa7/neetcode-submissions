class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        queue = deque()
        queue.append((0,0))
        visit = set()
        visit.add((0,0))
        length = 0
        R = len(grid)
        C = len(grid[0])
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if r == R - 1 and c == C - 1:
                    return length
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0 and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        queue.append((nr,nc))
            length += 1
        return -1