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
        # destructive.
        # length = n
        # [0, n-1, 1, n-2, 2, n-3, ...] <-- re-order in this format
        # O(n) time, O(n) space

        # merging two lists, reversing second half of list
        # getting middle
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        # reverse list from middle
        curr_slow = slow.next # capture second half
        slow.next = None # cut it in half.
        prev = None
        while curr_slow: 
            temp = curr_slow.next
            curr_slow.next = prev
            prev = curr_slow
            curr_slow = temp

        # first = [2, 4, 6, 8]
        # second = [8, 6]
        # merge two lists, in alternating order --> [2, 8, 4, 6]
        second = prev
        curr = head
        while second:
            firstNext = curr.next
            secondNext = second.next

            curr.next = second
            second.next = firstNext

            curr = firstNext
            second = secondNext