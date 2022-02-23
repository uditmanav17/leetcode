"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        maps = {}
        
        def dfs(node:"Node"):
            # create a new_node
            maps[node] = Node(node.val)
            
            # cover curr_node's neighbors
            for neighbor in node.neighbors:
                # if neighbor is not visited
                if neighbor not in maps:
                    # recurse dfs
                    dfs(neighbor)
                
                # add neighbor node -> maps[neighbor] 
                # to curr node's neighbors 
                maps[node].neighbors += [maps[neighbor]]
                
        dfs(node)
        
        return maps[node]
        
                