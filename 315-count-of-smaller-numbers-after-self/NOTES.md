[Binary Search](https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/2320000/Python3.-oror-binSearch-6-lines-w-explanation-oror-TM%3A-9784)
[Sorted Container](https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/1297647/Python-SortedList-solution-explained)
[SC hiepit](https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/1297775/Python-SortedList-Clean-and-Concise-O(NlogN)
​
**Approach**
Here's the plan:
1. Make arr, a sorted copy of the list nums.
2. iterate through nums. For each element num in nums:
- use a binary search to determine the count of elements in the arr that are less than num.
- append that count to the answer list
- delete num from arr
3. return the ans list
4. For example, suppose nums = [5,2,6,1] Then arr = [1,2,5,6].
- num = 5 => binsearch: arr = [1,2,/\5,6], i = 2 => ans = [2,_,_,_], del 5
- num = 2 => binsearch: arr = [1,/\2,6],   i = 1 => ans = [2,1,_,_], del 2
- num = 6 => binsearch: arr = [1,/\6],     i = 1 => ans = [2,1,1,_], del 6
- num = 1 => binsearch: arr = [/\1],       i = 0 => ans = [2,1,1,0], del 1
​