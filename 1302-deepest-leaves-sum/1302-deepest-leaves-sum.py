# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        
        while q:
            total = 0
            for _ in range(len(q)):
                node = q.popleft()

                total += node.val

                for child in [node.left, node.right]:
                    if child:
                        q.append(child)
                
        return total
        