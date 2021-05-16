# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkSymmetry(self, p : TreeNode, q : TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.checkSymmetry(p.left, q.right) and self.checkSymmetry(p.right, q.left)
        return p is q

    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left and root.right:
            return self.checkSymmetry(root.left, root.right)
        return root.left is root.right


        