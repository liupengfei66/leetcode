# https://leetcode-cn.com/problems/ransom-note/
# 解法1：利用collections.Counter的特性
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        x = c1 - c2
        # x只保留值大于0的符号，当c1里面的符号个数小于c2时，不会被保留
        # 所以x只保留下了，magazine不能表达的
        if len(x) == 0:
            return True
        else:
            return False

# 解法2：采用数组
# 先计算magazine里的字符数量，然后在ransom里出现一次就减一次，如果结果小于0了，那么证明magazine不够用了
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26
        for char in magazine:
            record[ord(char)-ord('a')] += 1

        for char in ransomNote:
            record[ord(char)-ord('a')] -= 1
            if record[ord(char)-ord('a')] < 0:
                return False
        return True
