# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # BFS can be used to identify the rightmost nodes at each level
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            curr_len = len(queue) # grab length of current level on the tree
            ans.append(queue[-1].val)

            for _ in range(curr_len): # iterate through the level
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return ans
        