class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        replacement = color
        if original == replacement: return image
        R = len(image)
        C = len(image[0])
        def dfs(r , c):
            if r < 0 or c < 0 or r >= R or c >= C or image[r][c] != original:
                return
            image[r][c] = replacement
            dfs(r + 1 , c)
            dfs( r - 1 , c)
            dfs(r , c - 1)
            dfs(r , c + 1)
            return 
        dfs(sr, sc)
        return image