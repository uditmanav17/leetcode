- Same as Pascal's Triangle Simulation
​
What we need to do in this problem is to simulate our pouring process: imagine, that we have `6` cups of water arrived at some place, then one full cup is left on this place and `2.5` cups go to the right bottom and left bottom cups. What we need to do now is to simulate this process!
​
- We start with `l = [poured]` -> top layer
- Then we process full current layer to create next layer. We need to check if we have enough champagne: if we have less than `1`, this cup is dead-end. If it has more than `1`, then we add values to bottom layer.
​
**Complexity**: time complexity is `O(R^2)`, where `R = query_row`, space complexity is `O(R)`.
​