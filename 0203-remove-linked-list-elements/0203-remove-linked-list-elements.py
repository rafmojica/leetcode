# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # initialize a dummy node (since val can be at the beginning)
        # initialize two pointers (one after the other. ptr and nextPtr)
        # 1. if nextPtr.val == val, continuously skip until we hit a node != val
        # 2. if we do, reassign pointer to nextPtr, increment ptr and nextPtr.
        # 3. terminate when nextPtr == None

        dummy = ListNode(0, head)
        ptr = dummy
        nextPtr = ptr.next

        while nextPtr:
            while nextPtr and nextPtr.val == val:
                nextPtr = nextPtr.next
            else:
                ptr.next = nextPtr
                
                if nextPtr is not None:
                    ptr = ptr.next
                    nextPtr = nextPtr.next

        return dummy.next
