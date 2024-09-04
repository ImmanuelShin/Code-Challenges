# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = []
        queue.append((1 , root))
        cur = 1
        prev = None
        res = []
        while(len(queue) > 0):
            h, node = queue.pop(0)
            if cur is not h:
                res.append(prev.val)
                cur = h
            if node.left is not None:
                queue.append((h + 1, node.left))
            if node.right is not None:
                queue.append((h + 1, node.right))
            prev = node
            if len(queue) == 0:
                res.append(prev.val)
        return res
