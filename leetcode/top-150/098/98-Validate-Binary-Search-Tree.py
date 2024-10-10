# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cur = float('-inf')
        self.res = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return
        self.isValidBST(root.left)
        if root.val <= self.cur:
            self.res = False
        else:
            self.cur = root.val 
        self.isValidBST(root.right)
        return self.res
