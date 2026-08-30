class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root,list1):
            if not root:
                return 
            inorder(root.left, list1)
            list1.append(root.val)
            inorder(root.right, list1)
            return list1
        
        result = inorder(root,[])
        return result[k-1]