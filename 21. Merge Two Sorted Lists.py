# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        #Recursive
        if l1 is None: return l2
        if l2 is None: return l1
        
        if l1.val < l2.val :
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
        """

        #Iterative
        head = tail = ListNode(0,None)

        while l1 and l2:
            if l1.val<l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next
        
        if l1: tail.next = l1
        else: tail.next = l2

        return head.next
                
