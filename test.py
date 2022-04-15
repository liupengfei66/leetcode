from typing import List
import collections

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        sum1 = collections.defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum1[i+j] += 1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                if -(i+j) in sum1:
                    res += 1
        return res

s = Solution()
s.fourSumCount([1,2], [-2,-1], [-1,2], [0,2])