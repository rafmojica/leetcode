# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        kFirst = dummy
        kEnd = dummy
        end = dummy

        for _ in range(k):
            kFirst = kFirst.next
            end = end.next

        while end:
            end = end.next
            kEnd = kEnd.next

        kEndVal = kEnd.val
        kEnd.val = kFirst.val
        kFirst.val = kEndVal

        return dummy.next
