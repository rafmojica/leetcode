# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # O(n) time, O(n) space
        # go to middle of list
        # reverse second half of list
        # merge the two results

        # get to the middle
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half of list [1, 2, 3, 4, 5] --> [5, 4]
        half = slow.next # [4, 5]
        slow.next = None
        prev = None
        while half:
            nxt = half.next # save next temporarily
            half.next = prev
            prev = half
            half = nxt

        # merge and alternate two lists
        # head = [1, 2, 3, 4, 5]
        # prev = [5, 4]
        # [1, 5, 2, 4, 3]    
        second = prev
        curr = head
        while second:
            firstNext = curr.next
            secondNext = second.next

            curr.next = second
            second.next = firstNext

            curr = firstNext
            second = secondNext
