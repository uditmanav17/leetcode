https://leetcode.com/problems/peeking-iterator/discuss/1055803/Python-Simple-solution-explained
​
This is more design problem, not algorithmic one in my opinion. You already given implemented class `iterator`, which you can understand as list, but it is not list. The goal is to implement so-called peeking iterator and to do this we need to be one step ahead: let us create `self.buffer` variable, which will keep next value from our iterator.
​
- When we call `peek` function, we just return value from our buffer.
- When we call `next` function, we write buffer variable to `tmp`, then we update our buffer: if we have next element, we go to the next element, if we do not have it we make it equal to `None`.
- Finally, `hasNext` function now is just checking if buffer is empty or not.
​
**Complexity**: it is `O(1)` for all operations, if it was `O(1)` for original `iterator` class.
​
​