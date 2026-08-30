class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue.append((0,0))
        visit = set()
        visit.add((0,0))
        directions = [[0,1] , [0,-1] , [1,0] , [-1,0]]

        def bfs(queue , visit ,  grid ,  directions):
            length = 0
            R = len(grid)
            C = len(grid[0])
            while queue:
                for i in range(len(queue)):
                    r , c = queue.popleft()
                    if r == R - 1 and c == C - 1:
                        return length
                    for nr , nc in directions:
                        if r+nr<0 or c+nc <0 or r+nr>=len(grid) or c+nc>= len(grid[0]) or (r+nr,c+nc) in visit or grid[r+nr][c+nc] == 1:
                            continue
                        queue.append((r+nr,c+nc))
                        visit.add((r+nr,c+nc))
                length += 1
            return -1
        return bfs(queue , visit , grid , directions)
                
        