# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         
        tot_len = 0
        cur_node = head 
        while cur_node is not None: 
            tot_len += 1
            cur_node = cur_node.next

        # If removing head, reset 
        if tot_len == n:
            return head.next    
        # Go back to now "from start value" and set 
        cur_node = head 
        
        # Stop at the node before, setting to None or next depending
        if n == 1:
            for i in range(tot_len - n - 1): 
                cur_node = cur_node.next
            cur_node.next = None 
        else:
            for i in range(tot_len - n - 1): 
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
        
        return head 
