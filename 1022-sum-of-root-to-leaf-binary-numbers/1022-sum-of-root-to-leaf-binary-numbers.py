# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.total = 0
    
    def sumRootToLeaf(self, 
                      root: Optional[TreeNode], 
                      curr_val=None) -> int:
        if not root:
            return 0
        
        if curr_val is None:
            curr_val = []
        
        if not root.left and not root.right:
            self.total += int("".join(curr_val + [str(root.val)]), 2)
            return self.total
        
        if root.left:
            self.sumRootToLeaf(root.left, curr_val + [str(root.val)])
            
        if root.right:
            self.sumRootToLeaf(root.right, curr_val + [str(root.val)])
        
        return self.total
    