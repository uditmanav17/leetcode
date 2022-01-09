# https://leetcode.com/problems/delete-node-in-a-bst/discuss/821420/Python-O(h)-solution-explained

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None
        
        # search BST
        if node.val > key:
            node.left = self.deleteNode(node.left, key)
            
        elif node.val < key:
            node.right = self.deleteNode(node.right, key)
            
        else:  # node.val is matched with key
            # if only one child
            if not node.left:
                return node.right
            
            if not node.right:
                return node.left
            
            # if both child present
            if node.left and node.right:
                # get max from left sub tree or min from right sub tree
                temp = node.right
                while temp.left:
                    temp = temp.left  # get min of right sub tree
                # copy min val to curr node val
                node.val = temp.val
                # recurse on right sub tree
                node.right = self.deleteNode(node.right, node.val)
                
        return node

        