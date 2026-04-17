# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # two fast pointers
        fast = head
        slow = head
        curr = head
        prev = None # [1 -> None]

        # find middle (fast stops loop, putting slow in the middle)
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        # reverse from middle
        while slow is not None:
            originalNext = slow.next
            slow.next = prev
            prev = slow
            slow = originalNext

        # compare the two pointers
        while prev is not None:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
        return True
