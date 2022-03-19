https://leetcode.com/problems/maximum-frequency-stack/discuss/1862015/BEST-Explanation-Visually
​
https://leetcode.com/problems/maximum-frequency-stack/discuss/1862029/python-O(1)-solution-list-of-stacks
​
Check Solution approach -
​
- Construct and maintain a the list of stacks (stks), where the ith element is the stack of values that have appeared i+1 times. The order of elements in the same stack follows the order in which they are pushed.
- For example, with the pushed series [5,5,3,4,4,5], stks will be [[5,3,4], [5,4], [5]].
- During the pop calls, we will just pop from the top of the last stack.
- This can be constructed and maintained easily during the push and pop calls.
​
**Time complexity: O(1)
Space complexity: O(N)**
​