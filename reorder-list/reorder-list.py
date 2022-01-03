# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_ll_mid(self, head):
        n = 0
        head_2 = head
        while head:
            n += 1
            head = head.next

        if n <= 2:
            return None
        
        n = (n // 2)
        while n:
            if n == 1:
                temp_node = head_2
            n -= 1
            head_2 = head_2.next
        
        # print("temp_node.val", temp_node.val)
        temp_node.next = None
        return head_2
    
    def reverse_ll(self, head):
        prev, curr = None, head
        
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        return prev
            
        
    def interleave_ll(self, l1, l2):
        head1, head2 = l1, l2
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt            
            
        
    def print_ll(self, head):
        while head:
            print(head.val, end='->')
            head = head.next
        print()


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy_head = head
        second_list_head = self.find_ll_mid(dummy_head)
        # print(dummy_head.val, second_list_head.val)
        if second_list_head is None:
            return head
        
        reversed_ll = self.reverse_ll(second_list_head)
        
        # self.print_ll(head)
        # self.print_ll(reversed_ll)
                   
        self.interleave_ll(head, reversed_ll)
        
        
            
        
        
        
        