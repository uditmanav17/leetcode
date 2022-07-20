https://leetcode.com/problems/number-of-matching-subsequences/discuss/1289526/Short-and-Easy-Solution-w-Explanation-or-Map-and-Binary-Search
​
​
We can see that checking if a word is subsequence of s is nothing but ensuring each character of the word occurs in s one after other (i.e, same order). We already have the ordering and indices of all characters in s from start itself.
​
So, instead of iterating over s each time, we could just iterate over it once and store indices of each character in increasing order. Thereafter, while checking if a word is subsequence, we will just search if there exists an index in s, for each character of given word, that's greater than the index found for previous charcter.
​
Since we have stored the indices for each character in sorted order, we would just apply binary search over a character's index array instead of linear search. If all characters of given word are found to have corresponding indices in s in an increasing order, we say that word is subsequence of s.