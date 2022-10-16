# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head and not head.next: return None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        p = head
        while p and p.next and p.next != slow:
            p = p.next
        
        p.next = p.next.next
        return head