Approach 1 -
- Compute interval (start, end) for each letter [a-z],
- where start is first occurrence of letter, and end is last occurrence of letter.
- Then we merge any overlapping intervals,
- and the resulting intervals can form the answer.
​
​
Appraoch 2 -
https://leetcode.com/problems/partition-labels/discuss/828031/Python-Greedy-O(n)-solution-explained
- First, we need to know all ends for each letter in advance, I call it ends.
- Also, `curr` is current index and last is index we need to traverse until. For each group of symbols we need to do: `last = ends[S[curr]]`: we find the place we need to traverse; while we do no reach this place, we look at the next symbol and update our `last`. So, we stop, when `curr` become greater than `last`.
- We add `curr` to our out result.
- Note, that we need to have `[8,7,8]` for our example, but we get `[8,15,23]`, places where our partitions are. So, we evaluate differences `8-0, 15-8, 23-15` and return them.
​
​
​