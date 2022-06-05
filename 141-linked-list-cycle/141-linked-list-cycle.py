# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
        
        slow = head
        fast = slow.next
        
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
            
        return fast == slow
            
        