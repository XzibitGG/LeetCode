# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPathSum(self, root: TreeNode, targetSum: int) -> bool:
        leftSum = self.getPathSum(root.left, targetSum - root.val) if root.left else None
        rightSum = self.getPathSum(root.right, targetSum - root.val) if root.right else None     
        if root.left and root.right:
            return leftSum or rightSum
        else:
            return leftSum if root.left else rightSum if root.right else root.val == targetSum


    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.getPathSum(root, targetSum) if root else False


        