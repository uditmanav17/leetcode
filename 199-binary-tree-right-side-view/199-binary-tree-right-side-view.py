# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return 
        view = {}
        q = deque([(0, root)])
        
        while q:
            height, node = q.popleft()
            view[height] = node.val
            
            for child in [node.left, node.right]:
                if child:
                    q.append((height + 1, child))
                    
        
        return view.values()
    