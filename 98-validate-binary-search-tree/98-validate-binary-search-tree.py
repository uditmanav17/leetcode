# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, node: TreeNode, minVal=float("-inf"), maxVal=float("inf")) -> bool:
        if node is None:
            return True
        
        if node.val <= minVal or node.val >= maxVal:
            return False
        
        l = self.isValidBST(node.left, minVal, node.val)
        r = self.isValidBST(node.right, node.val, maxVal)
        
        return l and r
        
        
        