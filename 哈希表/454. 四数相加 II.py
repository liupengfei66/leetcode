# https://leetcode-cn.com/problems/4sum-ii/
# 这题的思路很像1.两数之和，也就是先算两个数组的和，再算另外两个数组的和是否能凑够剩余的
# 对比0015.三数之和，0018.四数之和
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)
        for i in nums1:
            for j in nums2:
                hashmap[i+j] += 1

        res = 0
        for i in nums3:
            for j in nums4:
                target = 0 - (i + j)
                if target in hashmap:
                    res += hashmap[target]
        return res