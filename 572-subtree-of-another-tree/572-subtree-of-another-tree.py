# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeCheck(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if (root1 and not root2) or (root2 and not root1):
            return False
        
        return root1.val == root2.val \
    and self.subtreeCheck(root1.left, root2.left) \
    and self.subtreeCheck(root1.right, root2.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return 
        
        check = False
        if root.val == subRoot.val:
            check = self.subtreeCheck(root, subRoot)
                
        return check \
    or self.isSubtree(root.left, subRoot) \
    or self.isSubtree(root.right, subRoot)
            
            
        