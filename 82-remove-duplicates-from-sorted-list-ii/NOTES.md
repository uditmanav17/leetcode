Approach 1: Sentinel Head + Predecessor
​
- sentinel = predecessor = the last node before the sublist of duplicates
- if it's a beginning of duplicates sublist skip all duplicates
- move till the end of duplicates sublist
- skip all duplicates
- otherwise, move predecessor
- move head forward
​