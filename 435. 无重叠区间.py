# https://leetcode-cn.com/problems/non-overlapping-intervals/
# 这题的思想与452 引爆气球的很像
# 区别在于，这里的思想是区间个数-独立的区间个数=需要移除的区间数
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 1 # res 表示有多少个独立区间
        for i in range(len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                res += 1
            else:
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
        return len(intervals) - res