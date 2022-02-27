# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = deque([(root, 0)])
        max_ = 0
        
        while q:
            max_ = max(max_, q[-1][1] - q[0][1] + 1)
            temp_q = deque([])
            
            for node, node_idx in q:
                if node.left:
                    temp_q.append((node.left, 2 * node_idx))
                if node.right:
                    temp_q.append((node.right, 2 * node_idx + 1))
            q = temp_q
                    
                
        return max_

