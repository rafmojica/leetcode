# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prev = None

        for _ in range(left - 1): # prev is always behind curr.
            prev = curr
            curr = curr.next

        newTail = curr # save node at left position
        newHead = prev # save node before left position

        for _ in range(right - left + 1): # reverse
            oldNext = curr.next
            curr.next = prev
            prev = curr
            curr = oldNext

        # reconnect the old list to the new reversed list.
        if newHead:
            newHead.next = prev
        else:
            head = prev

        newTail.next = curr
        return head        
        