# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, 
                      cloned: TreeNode, 
                      target: TreeNode) -> TreeNode:
        
        q = deque([(original, cloned)])
        
        while q:
            o, c = q.popleft()
            if o is target:
                return c
            
            for o_node, c_node in [(o.left, c.left), (o.right, c.right)]:
                if o_node:
                    q.append((o_node, c_node))
            
        
        