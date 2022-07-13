# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        
        heights = {}
        q = deque([(0, root)])
        
        while q:
            curr_h, curr_node = q.popleft()
            heights.setdefault(curr_h,[])
            heights[curr_h].append(curr_node.val)
            
            for child in [curr_node.left, curr_node.right]:
                if child:
                    q.append((curr_h + 1, child))
                    
        return heights.values()
        