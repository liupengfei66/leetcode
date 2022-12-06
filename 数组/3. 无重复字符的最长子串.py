# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 滑动窗口
# 时间复杂度O(N)，滑动窗口对于每个元素都是进出一次，所以复杂度也是O(N)
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        queue = collections.deque([])
        res = 1
        for i in range(len(s)):
            # 只要新元素在队列中有重复，那么前面的都要出队列
            while s[i] in queue:
                queue.popleft()
            queue.append(s[i])
            res = max(len(queue), res)

        return res
