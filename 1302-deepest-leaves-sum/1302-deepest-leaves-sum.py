# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        height_sum = {}
        
        q = deque([(root, 0)])
        while q:
            node, curr_h = q.popleft()
            
            height_sum.setdefault(curr_h, 0)
            height_sum[curr_h] += node.val
            
            for child in [node.left, node.right]:
                if child:
                    q.append((child, curr_h + 1))
                
        return height_sum[max(height_sum)]
        