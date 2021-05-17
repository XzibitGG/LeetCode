# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        mid = len(nums) // 2
        root = TreeNode(val = nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid]) if len(nums[:mid]) != 0 else None
        root.right = self.sortedArrayToBST(nums[mid + 1:]) if len(nums[mid + 1:]) != 0 else None                                              
        return root


        