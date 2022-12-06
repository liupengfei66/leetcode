# https://leetcode-cn.com/problems/merge-intervals/
# 这题很像452. 引爆气球和435. 无重叠区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
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