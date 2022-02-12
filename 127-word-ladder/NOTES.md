So, we gonna see if we change first character c to another character to form a word. So, we gonna try ae , be, ce which is already in our set doesn't count de, ee all the ay down to ze and none of the word included inside our word list.
​
![](https://assets.leetcode.com/users/images/e580b3e4-5ebd-46e7-b546-f63e46749ed1_1644633248.873971.png)
​
Now we gonna see if we change e from ce to another character.
​
So, we gonna try ca, cb and so on..... eventually we get to the word co which is in our word list. So what that means we gonna add co to our queue & our set.
​
![](https://assets.leetcode.com/users/images/10697e6c-f2a9-4631-bb8f-271a0d4ca139_1644633282.432196.png)
​
Then we gonna pull from our queue again, in this case it would be me
​
Now from me we can go to mo by changing e from me to o from mo. So, we gonna add mo to our queue and our set.
​
![](https://assets.leetcode.com/users/images/ad0a8570-27f4-4e75-8ac9-dd6d5f16c8ba_1644633419.043082.png)
​
```
Another, thing i forgot to mention is our changes variable is being updated on every iteration.
So, we have gone from be -> ce -> co which is a total of 3 changes.
```
So, we gonna pull from our queue again co, now we can go from co to ko by changing c to k. So, what that mean's we need to add ko inside our queue and our set. And we increase our changes variable by 1
​
![](https://assets.leetcode.com/users/images/930fbdd7-774e-4384-93da-be75ee4b31be_1644633808.140633.png)
​
Now we pull from our queue again, which would be mo. We can get from mo -> ko by changing m to k. However, ko is already in our set. So, that mean's we gonna pull from our queue again which in this case would be ko.
​
```
queue = [  ]
changes = 4
set = ["be", "ce", "me", "co", "mo", "ko"  ]
```
And that is our end word. Once, we find our end word we poll from our queue and that is equal end word then we know we have found our shortest path sequence, so we just return 4 from this function.
​
ANALYSIS :-
**Time Complexity** :- BigO(M^2 * N), where M is size of dequeued word & N is size of our word list
**Space Complexity** :- BigO(M * N) where M is no. of character that we had in our string & N is the size of our wordList.