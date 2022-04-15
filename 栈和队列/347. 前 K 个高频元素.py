# https://leetcode-cn.com/problems/top-k-frequent-elements/
# 解法1：自带API
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = collections.Counter(nums)
        orderd = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            res.append(orderd[i][0])
        return res