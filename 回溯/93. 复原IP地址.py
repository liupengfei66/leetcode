# https://leetcode-cn.com/problems/restore-ip-addresses/submissions/
# 因为总共4段，所以前面只需要递归3次，直接判断最后一个字符串是否合法
# 其他都与77一样，就是剪枝的策略不同
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []

        def isValid(s):
            if len(s) == 0:
                return False
            if len(s) > 1 and s[0] == '0':
                return False
            if int(s) > 255:
                return False
            return True

        def backTracking(s, start):
            if len(path) == 3:
                last = s[start: len(s)]
                if isValid(last):
                    # 注意不能直接加入path，因为没有递归进入下一层
                    tmp = path[:]
                    tmp.append(last)
                    res.append(".".join(tmp))
                return
            # IP地址最多也就3个数字，超过了也就错了
            for i in range(start, min(start+3, len(s))):
                curr = s[start: i + 1]
                # 如果当前值已经不满足，那么再往后切分，也不可能满足
                if not isValid(curr):
                    break
                path.append(curr)
                backTracking(s, i + 1)
                path.pop()

        backTracking(s, 0)
        return res

