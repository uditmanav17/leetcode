# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return head
        slow = head
        fast = head.next
        
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
            
        if fast != slow:
            return None
        
        fast = head
        slow = slow.next
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
            
        
        
        