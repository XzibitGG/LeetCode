# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subDepth(self, root : TreeNode, depth : int) -> int:
        if root.left and root.right:
            return max(self.subDepth(root.left, depth + 1), self.subDepth(root.right, depth + 1))
        elif root.left:
            return self.subDepth(root.left, depth + 1)
        elif root.right:
            return self.subDepth(root.right, depth + 1)
        return depth

    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return self.subDepth(root, 1)
        return 0

        