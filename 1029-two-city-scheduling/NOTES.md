https://leetcode.com/problems/two-city-scheduling/discuss/667781/Python-3-Lines-O(n-log-n)-with-sort-explained
​
Let us first send all the people to the first city. Now, we need to choose half of them and change their city from first to second. Which ones we need to choose? Obviously the half with the smallest **difference** of costs between second and first cities. This difference can be negative and positive. Let us go through example: `costs = [[10,20],[30,200],[400,50],[30,20]]`
Then:
1. We put all of them to 1 city and pay `10 + 30 + 400 + 30`
2. Now, evaluate differences: `10, 170, -350, -10`
3. Choose 2 smallest differences, in this case it is `-350 and -10` (they are negative, so we can say we get a refund)
4. Evaluate final sum as `10 + 30 + 400 + 30` + `-350 + -10 = 110`
​
Complexity is `O(n log n)`, because we need to make one sort, and O(n) for evaluating differences and two sums. Space complexity is O(n), because we need to keep array of differences.