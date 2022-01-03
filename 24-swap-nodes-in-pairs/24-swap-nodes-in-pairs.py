# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        newPtr = head.next.next
        newHead = head.next
        newHead.next = head
        head.next = self.swapPairs(newPtr)
        
        return newHead
        