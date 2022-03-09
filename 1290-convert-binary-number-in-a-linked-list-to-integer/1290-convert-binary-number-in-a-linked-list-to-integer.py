# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        num = 0
        while head:
            val = head.val
            
            num <<= 1
            num |= val
            
            head = head.next 
            
        return num
        