https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Binary-search-Clean-and-Concise
​
I've added my long-ass proof here: https://leetcode.com/problems/path-with-minimum-effort/discuss/913076/python-Using-union-find-(Anyone-else-use-this-approach)
​
https://leetcode.com/problems/path-with-minimum-effort/discuss/1035940/Python-dfs-with-binary-search-explained
​
**Dijikstra**
- If we observe, this problem is to find the **shortest path** from a source cell `(0, 0)` to a destination cell `(m-1, n-1)`. Here, the shortest path is the one with m**inimum distance,** and **distance** is defined as **maximum absolute difference** in heights between two consecutive cells of the path.
- Thus, we could use Dijikstra's algorithm which is used to find the shortest path in a weighted graph with a slight modification of criteria for the shortest path, which costs `O(E log V)`, where `E` is number of edges `E = 4*M*N`, `V` is number of veritices `V = M*N`
​
​