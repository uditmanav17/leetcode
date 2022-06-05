# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def depthHelper(self, node, depth=0):
        if not node:
            return depth

        left_depth = self.depthHelper(node.left, depth + 1)
        right_depth = self.depthHelper(node.right, depth + 1)

        return max(left_depth, right_depth)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depthHelper(root)
        
        