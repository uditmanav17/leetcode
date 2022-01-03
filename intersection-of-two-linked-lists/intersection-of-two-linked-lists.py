# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_ll_len(self, head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n
    
    def getIntersectionNode(self, 
                            headA: ListNode, 
                            headB: ListNode) -> Optional[ListNode]:
        
        l1 = self.get_ll_len(headA)
        l2 = self.get_ll_len(headB)
        
        if l1 > l2:
            while l1 != l2:
                l1 -= 1
                headA = headA.next
        else:
            while l2 != l1:
                l2 -= 1
                headB = headB.next
                
        while headA and headB:
            if headA is headB:
                return headA
            
            headA = headA.next
            headB = headB.next
            
            
        
                
        
        