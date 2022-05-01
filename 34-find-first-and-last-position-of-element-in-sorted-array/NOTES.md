**Approach**:
- Find insert position for `target` in `array`, this will be our `start` of range
- Find insert position for `target + 1` in `array`, this will be our `end` of range
- return `[left, right]` if `left < right` else `[-1, -1]`
​
​