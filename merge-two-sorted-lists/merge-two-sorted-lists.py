# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, 
                      h1: Optional[ListNode], 
                      h2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy
        
        while h1 or h2:
            if h1 and not h2:
                curr.next = h1
                break
                
            if h2 and not h1:
                curr.next = h2
                break
                
            if h1.val < h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
                
            curr = curr.next
            
        return dummy.next
                
            
                
                
            
            
        