# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next # prev is the node before the left position

        start = prev.next # start is at the left position
        for _ in range(right - left):
            oldNext = start.next
            start.next = oldNext.next
            oldNext.next = prev.next
            prev.next = oldNext
        
        return dummy.next
        