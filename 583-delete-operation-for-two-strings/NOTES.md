Algorithm
​
In order to determine the minimum number of delete operations needed, we can make use of the length of the longest common sequence among the two given strings `s1` and `s2`, say given by `lcs`. If we can find this `lcs` value, we can easily determine the required result as `m + n - 2*lcs`. Here, `m` and `n` refer to the length of the two given strings `s1` and `s2`.
​
The above equation works because in case of complete mismatch(i.e. if the two strings can't be equalized at all), the total number of delete operations required will be `m + n`. Now, if there is a common sequence among the two strings of length `lcs`, we need to do `lcs` lesser deletions in both the strings leading to a total of `2lcs` lesser deletions, which then leads to the above equation.