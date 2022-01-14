https://leetcode.com/problems/find-unique-binary-string/discuss/1418687/Detailed-Explanation-O(N)-short-concise-code-Cantor's-Diagonalization-Java-Python-C%2B%2B
​
The trick to do this question is somewhat similar to Cantor's Diagonalization.
​
Since we are given that number of bits in the number is equal to number of elements.
What we can do is we create a binary string which differs from first binary at 1st position, second binary at 2nd position, third binary at 3rd position,...and so on.
​
This will make sure that the binary we have made is unique (as it differs from all others at atleast one position).
​
We create an empty string first.
And simply iterate through the binary strings while putting the flipped bit of ith bit of "binary at ith position".