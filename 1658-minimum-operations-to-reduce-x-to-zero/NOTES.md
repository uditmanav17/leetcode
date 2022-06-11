https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/2136555/C%2B%2BPython-Simple-Solution-w-Explanation-or-Sliding-Window
​
**Solution I - Sliding Window [Accepted]**
​
We need to make `prefix_sum + suffix_sum = x`. But instead of this, finding a subarray whose sum is `sum(nums) - x` will do the job. Now we only need to maximize the length of this subarray to minimize the length of `prefix + suffix`, which can be done greedily. By doing this, we can get the minimum length, i.e., the minimum number of operations to reduce `x` to exactly `0` (if possible).
​
If you haven't heard the term "sliding window" before, visit this [link](https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples).
​
1. Let us take a sliding window whose ends are defined by `start_idx` and `end_idx`.
2. If the sum of this sliding window (subarray) exceeds the target, keep reducing the window size (by increasing `start_idx`) until its sum becomes <= `target`.
3. If the sum becomes equal to the target, compare the length, and store if it exceeds the previous length.
4. Return `-1` if the sum of the sliding window never becomes equal to `target`.
​
​