​
**Algorithm**
​
1. If we see a 0, we gotta start off things again
2. If we see a positive number :
2.1. Increase length of positive mutilpicative result till now.
2.2. Increase length of negative mutilpicative result till now, unless we had not encountered any negative before.
3. If we see a negative number:
3.1. It's time to swap positive and negative multiplicative results' lengths and do similar task as we did in above case.
4. In each iteration, use the length of positive mutilpicative result to compute answer.
​
Dry Run -
```
elements      :   9    5    8    2    -6    4    -3    0    2    -5    15    10    -7    9    -2
positive_len  :   1    2    3    4     0    1     7    0    1     0     1     2     5    6     5
negative_len  :   0    0    0    0     5    6     2    0    0     2     3     4     3    4     7
```