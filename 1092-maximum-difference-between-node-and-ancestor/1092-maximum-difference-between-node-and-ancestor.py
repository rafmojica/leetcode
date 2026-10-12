# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        # rather than comparing every difference, calculate max and min, then subtract them!
        if not root:
            return 0

        def dfs(root, curr_max, curr_min):
            if not root:
                return curr_max - curr_min

            curr_max = max(root.val, curr_max)
            curr_min = min(root.val, curr_min)
            left = dfs(root.left, curr_max, curr_min)
            right = dfs(root.right, curr_max, curr_min)

            return max(right, left)

        return dfs(root, root.val, root.val)
