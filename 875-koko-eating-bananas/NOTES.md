https://leetcode.com/problems/koko-eating-bananas/discuss/1704140/Python-short-binary-search-explained
​
The idea is given value mid, answer a question: can Koko eat all bananas within H hours. We need sum(ceil(i/mid) for i in piles) hours to eat all bananas. Then we just do binary search and find the first place, where time is <= H. We always keep invariant: time(beg) > H and time(end) <= H, we can do it, because function time is not-increasing.
​
Complexity
Time Complexity: O(N log W), where N is the number of piles, and W is the maximum size of a pile, space is O(1).