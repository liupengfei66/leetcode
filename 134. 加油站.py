# https://leetcode-cn.com/problems/gas-station/
# 解法1：暴力破解
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            rest = gas[i] - cost[i] # 记录剩余油量
            idx = (i + 1) % len(gas)
            while rest > 0 and idx != i:
                rest += gas[idx] - cost[idx] # 模拟以i为起点行驶一圈
                idx = (idx + 1) % len(gas)
            if rest >= 0 and idx == i:
                return i

        return -1

# 解法2：贪心
# 首先，如果总的加油量>总的消耗量，那肯定是可以跑完的
# 在可以跑完的基础上，计算每个位置，可以剩余的油量，并从起始位置累加剩余油量
# 如果累加剩余油量出现负数，那么证明，最后一步需要的消耗>前面累加的，需要累加更多
# 那么从下一个位置重新开始计算
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_sum, total_sum, res = 0, 0, 0
        for i in range(len(gas)):
            curr_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if curr_sum < 0:
                res = i + 1
                curr_sum = 0
        if total_sum < 0:
            return -1
        return res

