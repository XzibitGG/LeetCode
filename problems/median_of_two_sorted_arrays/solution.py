class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = nums1 + nums2
        while len(x) > 2:
            x.remove(max(x))
            x.remove(min(x))
        return x[0] if len(x) == 1 else (x[0] + x[1])/2