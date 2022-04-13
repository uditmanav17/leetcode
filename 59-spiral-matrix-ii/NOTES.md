https://leetcode.com/problems/spiral-matrix-ii/discuss/963128/Python-rotate-when-need-explained
​
Let us notice one clue property about our spiral matrix: first we need to go to the right and rotate clockwise 90 degrees, then we go down and again when we reached bottom, we rotate 90 degrees clockwise and so on. So, all we need to do is to rotate 90 degrees clockwise when we need:
​
- When we reached border of our matrix
- When we reached cell which is already filled.
​
Let `x, y` be coordinates on our `grid` and `dx, dy` is current direction we need to move. In geometrical sense, rotate by `90` degrees clockwise is written as `dx, dy = -dy, dx`.
​
Note, that `matrix[y][x]` is cell with coordinates `(x,y)`, which is not completely obvious.
​
**Complexity**: time complexity is `O(n^2)`, we process each element once. Space complexity is `O(n^2)` as well.
​
​