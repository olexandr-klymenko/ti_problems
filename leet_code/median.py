from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = sorted(nums1 + nums2)
        sn_length = len(sorted_nums)
        if sn_length % 2 != 0:
            return sorted_nums[sn_length // 2]
        return (sorted_nums[sn_length // 2 - 1] + sorted_nums[sn_length // 2]) / 2
