class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c,visited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            for dr , dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]):
                    dfs(nr,nc,visited)
        for c in range(cols):
            dfs(0,c,pacific)
        for r in range(rows):
            dfs(r,0,pacific)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)
        # Cells reachable from both oceans
        return [[r, c] for r, c in pacific & atlantic]