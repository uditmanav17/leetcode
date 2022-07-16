https://leetcode.com/problems/out-of-boundary-paths/discuss/1293727/Python-Short-dp-explained
​
Let `dp(N, i, j)` be number of solutions if we start from point `(i, j)` and we an make at most `N` steps. Then we need to consider the cases:
​
- If `i == m` or `j == n` or `i < 0` or `j < 0`, it means that we reached boundary, so we return `1`: we found one more path.
- If `N == 0`, it means, that we out of moves, and we did not reached boundary yet, so we return `0`.
- Finally, we try to make `4` steps to all directions and return sum of all number of options.
- Note, that we visit this `3-rd line` only if `N >= 1`, so when we call function with first argument `N-1`, number of moves never be negative.
​
​
**Complexity**
We have `O(m*n*N)` states with 4 moves from each state, so we have time and space complexity `O(m*n*N)`.
​