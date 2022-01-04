# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([(root, 0)])
        ans = {}
        
        while q:
            curr_node, curr_depth = q.popleft()
            ans[curr_depth] = curr_node.val
            
            for node in [curr_node.left, curr_node.right]:
                if node:
                    q.append((node, curr_depth + 1))
                    
        return [val for h, val in ans.items()]
        