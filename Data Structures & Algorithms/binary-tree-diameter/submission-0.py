class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def diameter(root):
            if not root:
                return 0
            left_high = diameter(root.left)
            right_high = diameter(root.right)
            self.res = max(self.res, left_high + right_high)
            return 1 + max(left_high, right_high)
        diameter(root)
        return self.res