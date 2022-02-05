# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop, heapify

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # add head of all lists in heap
        for idx, currList in enumerate(lists):
            # heap.append((currList.val, idx, currList))
            if currList:
                heappush(heap, (currList.val, idx, currList))
        
        # create sentinal node to return answer
        dummy = new_list = ListNode(0)
        
        while heap:
            # remove node with min val
            curr_val, curr_idx, node = heappop(heap)
            
            # add next node of current node in heap
            if node.next:
                next_node = node.next
                heappush(heap, (next_node.val, curr_idx, next_node))
            
            new_list.next = node
            new_list = new_list.next
            
        return dummy.next
