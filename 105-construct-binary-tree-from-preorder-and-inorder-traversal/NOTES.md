https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/1258585/Python-Intuitive-O(n)-solution-explained
​
In preorder we have root, left, right and in inorder we have left, root, right. Note that root is the first element in preorder traveral, we find it in the inorder traversal and hence we know number of elements in left and right parts, and hence we do a recursion, given two new lists for each left and right.
​
To make it faster we need couple of optimizations:
​
1. Be careful with memory, we need to give only 4 indexes: for beginning and end of current preorder and inorder, not full lists. In fact we will keep shifted end indexes, so for range [a, b] we will keep pair (a, b+1).
2. At the moment the most expensive part is to search element in list a lot. At the moment the worst time complexity can be O(n^2) (thoughO(n log n) in average which is not so bad). To make it O(n) we precalculate all places for elements only once (we can not have equal elements).
​
How our recursion will work now:
1. If we have empty list, return None: non-existing node.
2. Find the place ind of the first element in our preorder list, that is dic[preorder[pr_beg]].
3. Create root node with this element.
4. Recursively attach left and right children and return root. We can understand the lenghts of parts, using ind, and then evaluate indexes of preorder split, using this information: see diagramm below.
```
pr_beg, [pr_beg + 1, .... , pr_beg + ind - in_beg], [pr_beg + ind - in_beg + 1, ... , pr_end - 1]
[in_beg, ... , ind - 1], ind, [ind + 1, ..., in_end - 1]
```
​
Complexity
In the end function helper will be called in total n times, and each time will take just O(1) time, alsow we have O(n) time to create dic. so overall complexity is O(n). Space complexity is O(n) as well to keep our answer.