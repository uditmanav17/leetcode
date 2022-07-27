# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stk = deque([root]) if root else None
        
        while stk:
            node = stk.pop()
            for child in [node.right, node.left]:
                if child: stk.append(child)
            
            node.left = None
            node.right = stk[-1] if stk else None
            
        
        