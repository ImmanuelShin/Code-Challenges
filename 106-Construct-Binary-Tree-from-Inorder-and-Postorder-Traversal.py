# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) > 1:
            root_index = inorder.index(postorder[-1])
            in_left = inorder[:root_index]
            in_right = inorder[root_index + 1:]
            post_left = postorder[:root_index]
            post_right = postorder[root_index:-1]
            return TreeNode(postorder[-1], self.buildTree(in_left, post_left), self.buildTree(in_right, post_right))
        elif len(postorder) == 1:
            return TreeNode(postorder[0], None, None)
        else:
            return None