# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None: 
            return None 
        if list1 is None: 
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val: 
            output = ListNode(val=list1.val)
            list1 = list1.next 
        else:
            output = ListNode(val=list2.val)
            list2 = list2.next 

        head = output
        while list1 is not None or list2 is not None: 
            
            if list1 is None:
                output.next = list2
                list2 = list2.next 
            elif list2 is None:
                output.next = list1
                list1 = list1.next 
            
            elif list1.val < list2.val: 
                output.next = list1
                list1 = list1.next
            else: 
                output.next = list2
                list2 = list2.next
            
            output = output.next

        return head
