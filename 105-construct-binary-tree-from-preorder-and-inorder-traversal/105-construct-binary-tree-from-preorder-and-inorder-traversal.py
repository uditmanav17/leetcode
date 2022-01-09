# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/1258585/Python-Intuitive-O(n)-solution-explained


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, 
                  preorder: List[int], 
                  inorder: List[int]) -> TreeNode:
        
        def helper(pr_beg, pr_end, in_beg, in_end):
            if pr_end - pr_beg <= 0: return None
            
            ind = dic[preorder[pr_beg]]
            root = TreeNode(inorder[ind])  
            
            cut_point = pr_beg + 1 + ind - in_beg
            root.left  = helper(pr_beg + 1, cut_point, in_beg, ind)
            root.right = helper(cut_point, pr_end, ind + 1, in_end)
            
            return root
        
        dic = {elem: it for it, elem in enumerate(inorder)}  
        return helper(0, len(preorder), 0, len(inorder))
    
    