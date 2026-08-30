class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertTreeRecursive(root):
            if not root:
                return None
            # Swap children regardless of whether they are None
            root.left, root.right = root.right, root.left
            invertTreeRecursive(root.left)
            invertTreeRecursive(root.right)
            return root
        return invertTreeRecursive(root)