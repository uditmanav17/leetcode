Approach #2: Sliding Window [Accepted]
Intuition
​
For each `right`, call `opt(right)` the smallest `left` so that the product of the subarray `nums[left] * nums[left + 1] * ... * nums[right]` is less than `k`. `opt` is a monotone increasing function, so we can use a sliding window.
​
Algorithm
​
Our loop invariant is that `left` is the smallest value so that the product in the window `prod = nums[left] * nums[left + 1] * ... * nums[right]` is less than `k`.
​
For every right, we update `left` and `prod` to maintain this invariant. Then, the number of intervals with subarray product less than `k` and with right-most coordinate `right`, is `right - left + 1`. We'll count all of these for each value of `right`.