# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        visited.add(head)
        while head:
            if head.next not in visited: visited.add(head.next)
            else: return head.next
            head = head.next
        return head


