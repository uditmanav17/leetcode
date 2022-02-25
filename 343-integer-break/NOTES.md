https://leetcode.com/problems/integer-break/discuss/80832/Share-some-thought-process-about-this-problem
​
If we want to break a number, breaking it into 3s turns out to be the most efficient.
2^3 < 3^2
4^3 < 3^4
5^3 < 3^5
6^3 < 3^6
...
​
Therefore, intuitively, we want as many 3 as possible
if a number % 3 == 0, we just break it into 3s -> the product is Math.pow(3, n/3)
​
As for numbers % 3 == 1, we don't want the 'times * 1' in the end;
- borrowing a 3 is a natural thought.
- if we borrow a 3, 3 can be divided into
- case 1: 1 + 2 -> with the extra 1, we have 2*2 = 4
- case 2: (0) + 3 -> with the extra 1, we have 4
- turns out these two cases have the same results
- so, for numbers % 3 == 1 -> the result would be Math.pow(3, n/3-1)*4
​
Then we have the numbers % 3 == 2 left
- again, we try to borrow a 3,
- case 1: 1+2 -> with the extra 2, we have 1*5 or 3*2 => 3*2 is better
- case 2: 0+3 -> with the extra 2, we have 2*3 or 5 => 2*3 is better
- and we actually just end up with not borrowing at all!
- so we can just *2 if we have an extra 2 -> the result would be Math.pow(3, n/3)*2
​
Then, we have a couple corner cases two deal with since so far we only looked at numbers  that are larger than 3 -> luckily, we only have 2 and 3 left, which are pretty easy to figure out.
​
​