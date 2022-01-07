# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/1002902/Python-2-pointers-solution-explained

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        
        dummy = ListNode(0, head)
        fast, slow = head, dummy
        
        while fast:
            # while we have fast.next and its value is equal to fast, 
            # it means, than we have one more duplicate, so we move fast pointer to the right
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
                
            # slow.next equal to fast means, 
            # that we have only 1 element in group of duplicated elements, 
            # that is we do not need to delete it and we move both pointers to right
            if slow.next == fast:
                slow, fast = slow.next, fast.next
            else:
                # slow.next is not equal to fast means, 
                # that we need to skip group of duplicated elements: we create new connection: slow.next = fast.next, and also we allocate fast = slow.next. 
                # Note, that now we still have the original property: slow points to node before group of duplicated elements and fast will be the last element of this group (after while fast.next and fast.val == fast.next.val: line)
                slow.next = fast.next
                fast = slow.next
                
        return dummy.next
        
        
        
        