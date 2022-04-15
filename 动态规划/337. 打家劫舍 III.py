# https://leetcode-cn.com/problems/house-robber-iii/
# 树形DP
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def robTree(root: TreeNode):
            # root表示root结点能够盗取的最大金额
            if not root:
                # 第1个返回值-偷，第2个返回值-不偷
                return 0, 0
            left = robTree(root.left)
            right = robTree(root.right)
            # 处理当前结点，分为偷与不偷当前结点
            # 偷当前结点，那么两个孩子就不能偷，所以最大金额为
            var1 = root.val + left[1] + right[1]
            # 不偷当前结点，那么可以选择两个孩子去偷，注意这里是有可能同时偷两个孩子的，从示例2可以看出，可以同时偷左右孩子的
            # 所以每个孩子都可以选择偷与不偷
            var2 = max(left[0], left[1]) + max(right[0], right[1])
            return var1, var2

        res = robTree(root)
        return max(res[0], res[1])
