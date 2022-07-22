# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print_ll(self, head):
        while head:
            print(head.val, "->", end=" ")
            head = head.next
        print()
        
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt = lt_head = ListNode(0)
        gt = gt_head = ListNode(0)
        
        while head:
            next_node = head.next
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                gt.next = head
                gt = gt.next
            head.next = None
            head = next_node
            
        
        # self.print_ll(lt_head.next)
        # self.print_ll(gt_head.next)
        lt.next = gt_head.next
        # self.print_ll(lt_head.next)
        
        return lt_head.next
        