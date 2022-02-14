# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def bfs(self, root):
        if not root: return 0
        
        q = deque([(root, 1)])
        max_depth = -1
        
        while q:
            curr_node, depth = q.pop()
            for node in [curr_node.left, curr_node.right]:
                if node:
                    q.append((node, depth + 1))
                    
            max_depth = max(max_depth, depth)
        
        return max_depth
    
    
    def recursive(self, root):
        if not root:
            return 0
        
        left_height = self.recursive(root.left)
        right_height = self.recursive(root.right)
        
        return max(left_height, right_height) + 1
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return self.recursive(root)
        return self.bfs(root)
        

            
        