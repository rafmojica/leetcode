# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        kFirst = kEnd = end = dummy

        for _ in range(k):
            kFirst = kFirst.next
            end = end.next

        while end:
            end = end.next
            kEnd = kEnd.next

        kFirst.val, kEnd.val = kEnd.val, kFirst.val

        return dummy.next
