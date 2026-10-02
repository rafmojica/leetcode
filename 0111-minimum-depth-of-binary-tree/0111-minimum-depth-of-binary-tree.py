# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        # minimum number of nodes from the root to the leaf.
        def dfs(root):
            if not root:
                return 0

            # if one of the childs is null, recurse into the other.
            if not root.left:
                return dfs(root.right) + 1
            elif not root.right:
                return dfs(root.left) + 1

            # if both children exist, call both of them.
            return min(dfs(root.left), dfs(root.right)) + 1
        
        return dfs(root)
