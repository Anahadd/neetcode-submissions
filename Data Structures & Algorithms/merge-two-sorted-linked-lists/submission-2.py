# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 

        l = list1
        r = list2

        n = ListNode()
        head = n

        while l != None and r != None: 
            if l.val <= r.val:
                n.next = l
                l = l.next
            else:
                n.next = r
                r = r.next
            
            n = n.next

        if l != None:
            n.next = l 
        else:
            n.next = r

        return head.next




        




                

        
        

        
