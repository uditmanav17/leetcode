# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        first = second = head
        
        # 1-based indexing
        while k != 1:
            k -= 1
            first = first.next
            
        kth_first = first
        
        while first.next:
            first = first.next
            second = second.next
            
        kth_last = second
        
        kth_first.val, kth_last.val = kth_last.val, kth_first.val
        
        return head

