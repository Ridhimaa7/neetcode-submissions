class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            minimumNode = minNode(root.right)
            root.val = minimumNode.val
            root.right = self.deleteNode(root.right, minimumNode.val)
        return root