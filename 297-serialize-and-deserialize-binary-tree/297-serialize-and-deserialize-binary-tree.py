# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/396124/Python-very-easy-to-understand-recursive-preorder-with-comments

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        return f"{root.val} {self.serialize(root.left)} {self.serialize(root.right)}"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        def decode(q):
            if q[0] == '#':
                q.popleft()
                return None
            node = TreeNode(int(q.popleft()))
            # print(node.val, q)
            # deque - q is mutable, so q for left and right will be different
            node.left = decode(q)
            node.right = decode(q)
            return node
        
        return decode(collections.deque(data.split(' ')))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
