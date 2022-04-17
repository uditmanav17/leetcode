# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        
        order = []
        self.inOrderTrav(root, order)
        
        # print([node.val for node in order], root.val)
        
        for idx in range(1, len(order)):
            node = order[idx-1]
            node.left = None
            node.right = order[idx]
        
        order[-1].left = order[-1].right = None
        
        return order[0]
        
    def inOrderTrav(self, node, arr):
        if not node: return 
        
        self.inOrderTrav(node.left, arr)
        arr.append(node)
        self.inOrderTrav(node.right, arr)
            
        