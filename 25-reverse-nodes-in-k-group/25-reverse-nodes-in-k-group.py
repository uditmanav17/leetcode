# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_nodes(self, head, count):
        prev, curr = None, head
        
        while curr and count > 0:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
            count -= 1
        
        return prev, head
            
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # check if we have sufficient nodes to reverse
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        # if insufficient nodes return current list
        if count < k: return head
        
        reversed_list_head, reversed_list_tail = self.reverse_nodes(head, k)
        # print(reversed_list_head.val, reversed_list_tail.val)
        reversed_list_tail.next = self.reverseKGroup(node, k)
        
        return reversed_list_head
        
        
        
        