https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/1233823/2-Easy-peasy-cakewalk-optimised-video-whiteboard-solutions
​
https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/1233802/Python-Bitmask-solution-explained
​
**Approach**
- Calculate bit vector for each word
- Iterate over all combinations of words
- `AND` the bit vectors of these combinations
- if resultant vector = 0, update `ans = max(ans, len(w1) * len(w2))`
​
​
**Time complexity** is `O(n*s) + O(n^2)`, where s is the average length of word and n is number of words.
**Space complexity** is `O(n)`.
​
​