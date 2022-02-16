# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # atleast 2 nodes
        if not head or not head.next:
            return head
        
        p1 = head
        p2 = head.next
        p3 = p2.next
        
        new_head = p2
        new_head.next = p1
        p1.next = self.swapPairs(p3)
        
        return new_head
        
        
        