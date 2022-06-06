# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def get_ll_len(self, head):
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt
            
    
    def getIntersectionNode(self, headA: ListNode, 
                            headB: ListNode) -> Optional[ListNode]:
        len_1 = self.get_ll_len(headA)
        len_2 = self.get_ll_len(headB)
        
        diff = abs(len_1 - len_2)
        
        if len_1 > len_2:
            new_head = headA
            other_head = headB
        else:
            new_head = headB
            other_head = headA
            
        while diff:
            new_head = new_head.next
            diff -= 1
            
        while new_head != other_head:
            new_head = new_head.next
            other_head = other_head.next
            
        return other_head
        
        
        