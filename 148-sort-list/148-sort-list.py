# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def merge2sortedlists(self, l1, l2):
        
        final_head = ListNode(0)
        curr = final_head
        
        while l1 or l2:
            n1 = l1 if l1 else ListNode(999999)
            n2 = l2 if l2 else ListNode(999999)
            
            if n1.val < n2.val:
                curr.next = n1
                l1 = l1.next
            else:
                curr.next = n2
                l2 = l2.next
                
            curr = curr.next
            
        return final_head.next
    
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # split list in mid
        fast = slow = head
        
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            
        # set end of first half to None
        temp.next = None
            
        # recurse on both halves
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.merge2sortedlists(l1, l2)
        