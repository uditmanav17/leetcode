# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = []
        
    def pathSum(self, 
                root: Optional[TreeNode], 
                targetSum: int, 
                curr_ans=None) -> List[List[int]]:
        
        if curr_ans is None:
            curr_ans = []
            
        if root is None:
            return
            
        if root.left is None and root.right is None:
            temp_ans = curr_ans + [root.val]
            if sum(temp_ans) == targetSum:
                self.ans.append(temp_ans[:])
            return self.ans
        
        curr_ans.append(root.val)
        self.pathSum(root.left, targetSum, curr_ans)
        self.pathSum(root.right, targetSum, curr_ans)
        curr_ans.pop()
        
        return self.ans
        
        
        