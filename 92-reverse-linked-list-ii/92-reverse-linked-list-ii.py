# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        left -= 1
        # right -= 1
        nodes = nodes[:left] + nodes[left:right][::-1] + nodes[right:]
        
        for idx in range(1, len(nodes)):
            prev_node = nodes[idx-1]
            curr_node = nodes[idx]
            prev_node.next = curr_node
            curr_node.next = None
            
        return nodes[0]
            
        
        