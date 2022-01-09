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

    def deserialize(self, data, bracket_mappings=None):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        self.data = data
        if self.data[0] == '#': return None
        node = TreeNode(self.data[:self.data.find(' ')]) 
        node.left = self.deserialize(self.data[self.data.find(' ')+1:])
        node.right = self.deserialize(self.data[self.data.find(' ')+1:])
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
