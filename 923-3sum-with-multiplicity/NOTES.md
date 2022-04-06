https://leetcode.com/problems/3sum-with-multiplicity/discuss/1123498/Python-Combinatorics-solution-explained
​
Let us calculate `Counter(arr)`, that is how what is frequency of each number and then check `3` cases:
​
- All numbers `i < j < k` ar different: then we can check all possible permutations for numbers `i` and `j` and then check that for `k = target - i - j` we have `i < j < k`.
- For numbers `i, j, k` we have `i = j != k`. Then we have `c[i]*(c[i]-1)*c[target - 2*i]//2` number of options. Why? Because we need to choose `i` element twice, this is number of combinations with `2` elements from `c[i]` elements. Note, that I did not specify which of three indexes here is smaller and which is bigger, so here we cover all cases where exactly 2 indexes are equal.
- For numers `i, j, k` we have `i = j = k`. Here answer is `c[i]*(c[i]-1)*(c[i]-2)//6`: number of combinations with `3` elements from `c[i]` elements.
​
**Complexity**: time complexity is `O(n^2)`, where `n` is length of `arr`, because on first iteration we did `O(n^2)` and on second and third we did `O(n)`. Space complexity is `O(n)`.
​