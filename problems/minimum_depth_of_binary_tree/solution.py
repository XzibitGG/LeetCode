# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root : TreeNode, depth : int) -> int:
        if root.left and root.right:
            return min(self.getDepth(root.left, depth + 1), self.getDepth(root.right, depth + 1))
        elif root.left or root.right:
            return self.getDepth(root.left, depth + 1) if root.left else self.getDepth(root.right, depth + 1)
        return depth

    def minDepth(self, root: TreeNode) -> int:
        return self.getDepth(root, 1) if root else 0