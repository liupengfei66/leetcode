# https://leetcode-cn.com/problems/assign-cookies/
# 先满足胃口最小的小朋友，依次继续
# 亮点在于idx的应用，减少了一层for循环，同时减少了空间占用
# 时间复杂度：O(nlogn) - 快排O(nlogn)，遍历O(n)
# 空间复杂度：O(1)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx = 0
        for i, cookie in enumerate(s):
            if idx < len(g) and cookie >= g[idx]:
                idx += 1
        return idx

