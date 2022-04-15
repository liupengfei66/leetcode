# https://leetcode-cn.com/problems/reconstruct-itinerary/
# 难点：1. 如何判断终止条件？即到达的机场数=飞机票数+1
# 2. 如何找到一个路径就返回？在递归时，返回True，然后外层调用时，也遇到True就直接返回
# 3. 如何保证最小路径？对到达机场进行排序，先去小路径的机场
# 4. 如何保证不走重复路线？ 这里的解决方法是，在每次树枝遍历的时候，先删除掉走过的路线，然后回溯时再恢复，但这种修改了正在使用的map，容易出错
# 另外一种方法是同时记录到达机场和走过的次数，次数为0时，不再继续
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        trips = collections.defaultdict(list)
        for ticket in tickets:
            trips[ticket[0]].append(ticket[1])
        path = ["JFK"]

        def backTracking(start_place):
            # 到达的机场数=飞机票数+1，证明所有票都用过了
            # 直接返回
            if len(path) == len(tickets) + 1:
                return True
                # 先对到达进场进行排序，保证第一个满足条件的序列是最小的
            trips[start_place].sort()
            for _ in trips[start_place]:
                # 在当前树枝搜索时，进行过的航线就删除，保证不会重复
                end_place = trips[start_place].pop(0)
                path.append(end_place)
                if backTracking(end_place):
                    return True
                path.pop()
                # 回溯时，需要恢复该航线
                trips[start_place].append(end_place)

        backTracking("JFK")
        return path