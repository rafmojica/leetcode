# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # iterate through sllist, if the current node is the same as the previous,
        # skip it until we reach a unique value.
        # [1, 1, 2, 3, 3] --> [1, 2, 3]
        #  ^  ^
        # [1, 2, 3, 3]
        #     ^  ^
        pointer = head
        while pointer is not None and pointer.next is not None:
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head