https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/1204168/JS-Python-Java-C%2B%2B-or-Easy-4-Rectangles-DP-Solution-w-Explanation
​
Idea:
This problem brings up one of the characteristics of a 2D matrix: the sum of the elements in any rectangular range of a matrix (M) can be defined mathematically by the overlap of four other rectangular ranges that originate at M[0][0].
​
The sum of the rectangle (0,0)->(i,j) is equal to the cell (i,j), plus the rectangle (0,0)->(i,j-1), plus the rectangle (0,0)->(i-1,j), minus the rectangle (0,0)->(i-1,j-1). We subtract the last rectangle because it represents the overlap of the previous two rectangles that were added.
​
![Visual](https://i.imgur.com/tmTpvF5.gif)
​
With this information, we can use a dynamic programming (DP) approach to build a prefix sum matrix (dp) from M iteratively, where dp[i][j] will represent the sum of the rectangle (0,0)->(i,j). We'll add an extra row and column in order to prevent out-of-bounds issues at i-1 and j-1 (similar to a prefix sum array), and we'll fill dp with 0s.
​
At each cell, we'll add its value from M to the dp values of the cell on the left and the one above, which represent their respective rectangle sums, and then subtract from that the top-left diagonal value, which represents the overlapping rectangle of the previous two additions.
​
Then, we just reverse the process for sumRegion(): We start with the sum at dp[R2+1][C2+1] (due to the added row/column), then subtract the left and top rectangles before adding back in the doubly-subtracted top-left diagonal rectangle.
​
(Note: Even though the test cases will pass when using an int matrix for dp, the values of dp can range from -4e9 to 4e9 per the listed constraints, so we should use a data type capable of handling more than 32 bits.)
​
Time Complexity:
constructor: O(M * N) where M and N are the dimensions of the input matrix
sumRegion: O(1)
​
Space Complexity:
constructor: O(M * N) for the DP matrix
constructor: O(1) if you're able to modify the input and use an in-place DP approach
sumRegion: O(1)