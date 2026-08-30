# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = k - 1
        output = []
        stack = []
        curr = root
        if root == None:
            return []
        while curr or stack:
            if root:
                while curr:
                    stack.append(curr)
                    curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        return output[n]

        
        
        