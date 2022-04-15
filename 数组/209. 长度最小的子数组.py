# https://leetcode-cn.com/problems/minimum-size-subarray-sum/
# 滑动窗口 时间复杂度O(2*n)，空间复杂度O(1)
# 时间复杂度，每个元素都是进窗口一次，出窗口一次，所以是2*n，不是O(n*n)
# 主要难点在于窗口怎么去写，首先窗口的终止位置是很明显的
# 而每次满足total的时候，就开始移动窗口的起始位置，所以这种写法不难理解
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        start, total = 0, 0
        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                # 如果减去nums[start]依然满足条件，那么res会再被执行一次，会更新
                # 如果减去之后不满足条件，那么res其实是计算的减之前的位置
                # 所以res的更新是没问题的
                res = min(res, end - start + 1)
                total -= nums[start]
                start += 1

        return 0 if res == float('inf') else res




