# https://leetcode-cn.com/problems/partition-labels/
# 先找到每个字母最远的位置，如果能到达就直接分割
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        res = []
        pre_pos, max_dis = 0, 0
        for i in range(len(s)):
            hashmap[s[i]] = i
        for i in range(len(s)):
            if hashmap[s[i]] > max_dis:
                max_dis = hashmap[s[i]]
            if i == max_dis:
                res.append(i+1-pre_pos)
                pre_pos = i+1
        return res

