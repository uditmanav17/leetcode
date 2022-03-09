"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return 
        
        trav = []
        
        def recursive_helper(node):
            trav.append(node.val)
            
            for child in node.children:
                recursive_helper(child)
                
        
        recursive_helper(root)
        
        return trav
            
        
        
        