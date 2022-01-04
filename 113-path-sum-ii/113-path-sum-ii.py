# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        if not root:
            return []
        res = [root]
        answer = []
        self.pathSumHelper(root, total, res, answer)
        return answer

    def pathSumHelper(self, node, total, res, answer):
        if node.left is None and node.right is None and self.checkSum(res) == total:
            answer.append([node.val for node in res])

        if node.left:
            res.append(node.left)
            self.pathSumHelper(node.left, total, res, answer)
            res.pop()

        if node.right:
            res.append(node.right)
            self.pathSumHelper(node.right, total, res, answer)
            res.pop()

    def checkSum(self, li):
        return sum(node.val for node in li)
        