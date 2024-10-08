# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        def traverse(root, vals):
            if root is None:
                return
            traverse(root.left, vals)
            vals.append(root.val)
            traverse(root.right, vals)
        traverse(root, vals)
        return vals[k - 1]