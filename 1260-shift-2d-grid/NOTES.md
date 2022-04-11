https://leetcode.com/problems/shift-2d-grid/discuss/1934734/Python-In-place-Solution-with-Explanation
​
**Approach 1: GCD**
​
How then do we know if the loop will reach the initial index before all elements are swapped, and how many times do we need to increment the initial index? One way is to use the **greatest common divisor (GCD)** between the number of elements in `grid` and `k`, which gives us the number of times we need to increment the initial index.
​
TC: O(mn), since each index is looped through only once.
Note: for time complexity of math.gcd(), you can read more [here](https://codility.com/media/train/10-Gcd.pdf).
SC: O(1), as discussed previously.