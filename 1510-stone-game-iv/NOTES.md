https://leetcode.com/problems/stone-game-iv/discuss/1708369/Easy-Explanation-you-will-definitely-gonna-understand
​
![visual](https://assets.leetcode.com/users/images/01c43869-37d7-4612-a611-5e8ba0f20610_1642825595.5490935.png)
​
1. So, from 7 stones Alice 1st remove 1 stone & then Alice remove 4 stones
* When Alice remove 1 stone the remaining stone left is 6.
* But If Alice remove 4 stones then remaining stones left are 3.
2. Now it's Bob turn. Bob as well can make only 2 moves i.e. 1 OR 4 which is less than 6
* When Bob remove 1 stone from branch 6 the remaining stone left is 5. But If Bob remove 4 stones from branch 6 then remaining stones left are 2.
* But in Branch 3 Bob can only remove 1 stone, so remaining left is 2.
3. Now it's Alice turn.
* From branch 5 if Alice decide to remove 1 stone remaining stone left is 4. But, if alice decide to remove 4 stone remaining stone left is 1.
* From branch 2 if Alice decide to remove 1 stone remaining stone left is 1.
* From another branch 2 if Alice decide to remove 1 stone remaining stone left is 1
4. Now the Bob turn and every branch is ending with perfect square. So, Bob can remove from any branch because there is no branch from Alice can win.
​
So, as you see there are no. of repeated sub problems, like 2, 4 so we will use the Dynamic Programming to solve this problem.
​
https://leetcode.com/problems/stone-game-iv/discuss/909373/Python-DP-solution-using-game-theory-explained
​
In this problems we have game with two persons, and we need to understand who is winning, if they play with optimal strategies. In this game at each moment of time we have several (say k) stones, and we say that it is position in our game. At each step, each player can go from one position to another. Let us use classical definitions:
​
* The empty game (the game where there are no moves to be made) is a losing position.
* A position is a winning position if at least one of the positions that can be obtained from this position by a single move is a losing position.
* A position is a losing position if every position that can be obtained from this position by a single move is a winning position.
​
Why people use definitions like this? Imagine that we are in winning position, then there exists at least one move to losing position (property 2), so you make it and you force your opponent to be in loosing position. You opponent have no choice to return to winning position, because every position reached from losing position is winning (property 3). So, by following this strategy we can say, that for loosing positions Alice will loose and she will win for all other positions.
​
So, what we need to check now for position state: all positions, we can reach from it and if at least one of them is False, our position is winning and we can immedietly return True. If all of them are True, our position is loosing, and we return False. Also we return False, if it is our terminal position.
​
Complexity: For each of n positions we check at most sqrt(n) different moves, so overall time complexity is O(n sqrt(n)). Space complexity is O(n), we keep array of length n.