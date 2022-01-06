# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lca_node = None
    
    def lca_helper(self, node, p, q):
        if not node: 
            return False
        
        left = self.lca_helper(node.left, p, q)
        right = self.lca_helper(node.right, p, q)
        curr = node is p or node is q
        
        if (left + right + curr) == 2:
            self.lca_node = node
        
        return left or right or curr    
    
    def lowestCommonAncestor(self, 
                             root: 'TreeNode', 
                             p: 'TreeNode', 
                             q: 'TreeNode') -> 'TreeNode':
        
        self.lca_helper(root, p, q)
        return self.lca_node
    