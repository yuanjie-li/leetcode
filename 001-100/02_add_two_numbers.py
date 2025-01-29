# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initialize the first step
        # "given two non-empty linked lists"
        cur_node = ListNode()
        cur_node.val = (l1.val + l2.val) % 10
        output = cur_node

        # Set up for next iter
        carry = (l1.val + l2.val) // 10   
        l1 = l1.next 
        l2 = l2.next 
         
        while l1 is not None or l2 is not None or carry > 0: 

            # Get values and sum 
            new_node = ListNode() 
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            cur_val = l1_val + l2_val + carry 
            carry = cur_val // 10 
            new_node.val = cur_val % 10 

            cur_node.next = new_node
            cur_node = new_node 

            # Iterate the loop
            l1 = l1.next if l1 is not None else None 
            l2 = l2.next if l2 is not None else None 

        return output 
