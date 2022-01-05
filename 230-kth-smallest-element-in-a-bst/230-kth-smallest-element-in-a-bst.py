# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorderTrav = self.inorder(root)
        # print(inorderTrav)
        return inorderTrav[k-1]
        
    def inorder(self, node, arr=None):
        if arr is None:
            arr = []
            
        if not node:
            return
        
        self.inorder(node.left, arr)
        arr.append(node.val)
        self.inorder(node.right, arr)
        
        return arr
        