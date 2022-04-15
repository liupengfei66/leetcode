# https://leetcode-cn.com/problems/happy-number/
# 这题也没有看起来那么简单
# 主要思路是如果sum会重复，那么就会一直计算下去，不会出现1
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        n = str(n)
        while True:
            total = 0
            for num in n:
                total += int(num) * int(num)
            n = str(total)
            if total == 1:
                return True
            elif total in record:
                return False
            else:
                record.add(total)