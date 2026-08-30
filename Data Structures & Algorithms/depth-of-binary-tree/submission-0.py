class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maximumDepth(root):
            if not root:
                return 0
            totalleft = 1 + maximumDepth(root.left)
            totalright = 1 + maximumDepth(root.right)
            return max(totalleft, totalright)
        return maximumDepth(root)