# https://leetcode-cn.com/problems/merge-intervals/
# 这题很像452. 引爆气球和435. 无重叠区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            last = res[-1]
            # 有重叠, 合并区间 start修改为最小，end修改为最大
            if last[1] >= intervals[i][0]:
                res[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                res.append(intervals[i])
        return res