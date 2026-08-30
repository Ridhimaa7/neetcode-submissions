# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(root,currsum):
            if not root:
                return False
            if root.left is None and root.right is None:
                currsum += root.val
                return currsum == targetSum
            return backtrack(root.left,currsum + root.val) or backtrack(root.right,currsum + root.val)
        return backtrack(root, 0)