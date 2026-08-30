# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        res = []
        queue.append(root)
        curr = 0
        if root is None:
            return []
        while queue:
            res.append([])
            for _ in range(len(queue)):
                p = queue.pop(0)
                res[curr].append(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            curr += 1
        print(res)
        return [v[-1] for v in res]





        