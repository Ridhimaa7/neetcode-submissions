from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        def bfs(grid):
            visited = set()
            visited.add((0,0))
            length = 0
            queue = deque()
            queue.append((0,0))
            R = len(grid)
            C = len(grid[0])
            while queue:
                for i in range(len(queue)):
                    r , c = queue.popleft()
                    if r == R -1 and c == C -1:
                        return length
                    direction = [[0,1] , [1,0] , [0,-1] , [-1,0]]
                    for dr , dc in direction:
                        if r + dr < 0 or c + dc < 0 or r + dr >= R or c + dc >= C or (r+dr,c+dc) in visited or grid[r+dr][c + dc] == 1:
                            continue
                        queue.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))
                length += 1
            return -1
        return bfs(grid)

        
        
            

        