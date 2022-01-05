# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = {}
        if not root:
            return []
        self.traverse(root, ans)

        return [v if k % 2 == 0 else v[::-1] for k, v in sorted(ans.items())]

    def traverse(self, node: TreeNode, sol: dict, depth=0):
        if not node:
            return

        sol.setdefault(depth, [])
        sol[depth].append(node.val)
        self.traverse(node.left, sol, depth + 1)
        self.traverse(node.right, sol, depth + 1)

        