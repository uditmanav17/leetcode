https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/835323/Python-3-or-DP-or-Explanation
​
**Intuition**
- To find the frequency of the longest increasing sequence, we need
- First, know how long is the longest increasing sequence
- Second, count the frequency
- Thus, we create 2 lists with length `n`
- `dp[i]`: meaning length of longest increasing sequence
- `cnt[i]`: meaning frequency of longest increasing sequence
- If `dp[i] < dp[j] + 1` meaning we found a longer sequence and `dp[i]` need to be updated, then `cnt[i]` need to be updated to `cnt[j]`
- If `dp[i] == dp[j] + 1` meaning `dp[j] + 1` is one way to reach longest increasing sequence to i, so simple increment by `cnt[j]` like this `cnt[i] = cnt[i] + cnt[j]`
- Finally, sum up cnt of all longest increase sequence will be the solution
- This is a pretty standard DP question. Just like most sequence type of DP question, we need to loop over each element and check all previous stored information to update current.
- Time complexity is `O(n^2)`