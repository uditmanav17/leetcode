https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/1347895/Pyhton-O(h)-solution-explained
​
In this problem we have BST so we can use this property. We use dfs(root) function, and we can have options:
​
1. `root.val > max(p.val, q.val)`: in this case we do not have any option except of going to the `left`: all right subtree is too big for us because of BST property.
2. `root.val < min(p.val, q.val)`: in this case we go to the `right`, because all left subtree is too small.
3. Finally if we have `root.val` between `min(p.val, q.val)` and `max(p.val, q.val)`, it means that we found desired node
​
**Complexity**
Time and space complexity is `O(h)`: the height of our tree.
It can go upto n, but for balanced BST it is `O(log n)`.
​
​
​