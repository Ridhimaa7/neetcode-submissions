class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(r, c, i):
            if (r,c) in visited or r == len(board) or c == len(board[0]) or min(r,c) < 0 or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in directions:
               if dfs(r + dr, c + dc, i+1):
                return True
            visited.remove((r,c))
            return False
        for R in range(len(board)):
            for C in range(len(board[0])):
                if dfs(R,C,0):
                    return True
        return False