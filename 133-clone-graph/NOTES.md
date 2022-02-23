https://leetcode.com/problems/clone-graph/discuss/902767/Python-dfs-recursive-solution-explained
​
When you see the problem about graph, the first thing you need to think about is some classical graph traversal: dfs or bfs. Usually, there are 3 options with same complexities you can choose from:
​
1. Iterative dfs, that is dfs with stack
2. Recursive dfs, which is a bit simpler to code, but be careful if you have very deep graphs.
3. bfs - only iterative, there is no recursion version, because we use queue, not stack here.
​
Here we choose method number 2 (because it is easy to code of course)
​
Let us create global dictionary `mapping`, which will connect nodes from old graph with nodes from new graph and use recursive `dfs` function to construct these connections:
​
1. First, add connection `mapping[node] = Node(node.val)`
2. Traverse all neighbors of node and if node is not traversed, that is it is not in our mapping, then we run dfs for this neighbor. Also we add connection in new graph (we add it even if node is visited!)
​
**Complexity**: time complexity is `O(E)`: this number of iterations we need for full dfs traversal. Space complexity is `O(E+V) = O(E)` for connected graph.