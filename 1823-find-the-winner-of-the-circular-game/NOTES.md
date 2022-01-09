https://leetcode.com/problems/find-the-winner-of-the-circular-game/discuss/1152705/JavaC%2B%2BPython-4-lines-O(n)-time-O(1)-space
​
first step, we kick out kth item starts from position 0
then we make k+1 th item as first position, now we have i-1 items left, since we already know the result position of i-1 th item, we simply add its value from new starting point, which means k+res, you can also think of adjusting it's starting position.
in the end, take a mod, since it's circular.
​
if still question, take a example, k =2, i =3
1,2,3 -> 3 is winner, position 3
1,2,3,4 -> take 2 out first, we have 1,3,4 left
1,3,4 -> 3(position 2) is the starting point now, since we know for i-1(3) items, winner is at position 3, then take the mod, we know 1 is the winner
​