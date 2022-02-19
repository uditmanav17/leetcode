https://leetcode.com/problems/minimize-deviation-in-array/discuss/1781805/A-very-very-Highly-Detailed-EXPLANATION
​
https://leetcode.com/problems/minimize-deviation-in-array/discuss/1781862/C%2B%2B-or-Priority-Queue-or-Easy
​
- If the element is even, divide it by 2
- If the element is odd, multiply it by 2
- Convert odd numbers to even numbers by doubling it only once. Similarly, an even number can be divided multiple times to get an odd number. Therefore, the value of even numbers can never be increased.
- Data Structure used: Priority Queue (Max Heap)
​
**Algorithm**:
- Convert all odd numbers to even by multiplying it by 2 once
- Push all the elements into the priority queue
- While the queue is not empty and the maximum value is even, do:
- Update the difference (maxval - minval) constantly, while reducing the maxval/2.
- Push maxval/2 onto the heap.
- Similarly, update the minval on each operation.
- Return the minimum value between difference and the (value of top of queue - minval).
​
![](https://assets.leetcode.com/users/images/1c8061a8-32d8-4743-94f1-0ca770d96f37_1645241683.8619225.png)
​
Time Complexity : O(N(logN)(logM))
Space Complexity : O(N)