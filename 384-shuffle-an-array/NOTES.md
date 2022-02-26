https://leetcode.com/problems/shuffle-an-array/discuss/1350213/Python-Fisher-Yates-algorithm-explained
​
In this problem we need to shuffle given array and there are different ways to do it. The most optimal algorithm is called `Fisher-Yates` Algorithm, where we swap original array elements. The idea is to do several steps:
​
Take `i = 0` and then generate random index from `[0, n-1]` and swap these two elements.
Take `i = 1` and then generate random index from `[1, n-1]` and swap these two elements.
...
​
Actually this code is for Fisher-Yates with indexes from lowest to highest, classical one is in opposite direction, but this one a bit easirer to code. It is not obvious why this algorithm will generate all shuffles with the same probability, but it can be solved by induction, see wikipedia for more details.
​
Complexity
Time complexity is `O(n)` both for reset and shuffle. Space complexity is `O(n)`.