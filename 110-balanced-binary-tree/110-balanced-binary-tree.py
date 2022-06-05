# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced_helper(self, node):
        if not node:
            return True, 0
        
        l_balanced, l_height = self.isBalanced_helper(node.left)
        r_balanced, r_height = self.isBalanced_helper(node.right)
        
        curr_balanced = abs(l_height - r_height) <= 1
        # print(node.val, curr_balanced)
        
        return l_balanced and r_balanced and curr_balanced, max(l_height, r_height) + 1
    
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        a, b = self.isBalanced_helper(root)
        return a
        