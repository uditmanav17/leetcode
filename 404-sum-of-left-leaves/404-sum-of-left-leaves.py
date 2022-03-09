# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        q = deque([(root.left, root.right)])
        
        while q:
            l, r = q.popleft()
            
            if l and l.left is None and l.right is None:
                total += l.val
                
            for node in [l, r]:
                if node:
                    q.append((node.left, node.right))
                    
        return total
