https://leetcode.com/problems/remove-duplicate-letters/discuss/1859410/JavaC%2B%2B-DETAILED-%2B-VISUALLY-EXPLAINED-!!
​
![](https://assets.leetcode.com/users/images/20260c29-2873-4002-b1a1-5479f5d3eca3_1647569488.8472958.gif)
​
https://leetcode.com/problems/remove-duplicate-letters/discuss/1859515/Python-oror-O(n)-Beats-98-oror-Stack-oror-Detailed-Explanation-oror-Simple
​
last_occ = used to capture last occurence of any character in string
​
- We traverse sequentially on the string
- For each s[i], we check whether it's already in stack or not
- if its not in the stack, we need to push it to the stack. But we need to check another condition before pushing.
- If s[i] is not in the stack, and it is smaller than previous elements in stack (lexicographically), and those elements are repeating in future (can check with last_occ), we need to pop these elements
- Now we can push s[i] in stack
- Finally just join the characters in stack to form the result
​
Example:
s = 'bcabc'
last_occ = { a : 2, b : 3, c : 4 }
stack trace:
[]
[ 'b' ]
[ 'b', 'c' ]
[ 'a' ] (b & c got popped because a < c, a < b and b and c both were gonna repeat in future)
[ 'a' , 'b' ]
[ 'a' , 'b', 'c' ]
​
​