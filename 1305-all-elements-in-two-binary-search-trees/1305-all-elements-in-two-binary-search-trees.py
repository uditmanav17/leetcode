# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder_trav(node):
            if not node:
                return []
            return inorder_trav(node.left) + [node.val] + inorder_trav(node.right)
        
        seq1, seq2 = inorder_trav(root1), inorder_trav(root2)
        
        # python uses Tim sort, which identifies the two already sorted
        # runs as such and simply merges them. And since it's done in C, 
        # it's likely faster than if I tried merging myself in Python
        return sorted(seq1 + seq2)
        