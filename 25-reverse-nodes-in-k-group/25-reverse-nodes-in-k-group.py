# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
            
        n = len(nodes)
        for idx in range(0, n - (n % k), k):
            nodes[idx:idx+k] = reversed(nodes[idx:idx+k])
            
        for idx in range(1, len(nodes)):
            prev_node = nodes[idx-1]
            curr_node = nodes[idx]
            prev_node.next = curr_node
        
        nodes[-1].next = None
            
        return nodes[0]
