# https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/
# 贪心的思想就是，每次引爆交集最多的气球
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = 1
        for i in range(len(points)):
            # 如果当前气球的起始>前面气球的终止
            # 那么两个已经没有交集，需要新的箭
            if points[i][0] > points[i-1][1]:
                res += 1
            else:
                # 有交集的情况下，我们取最短的距离
                points[i][1] = min(points[i][1], points[i-1][1])
        return res

