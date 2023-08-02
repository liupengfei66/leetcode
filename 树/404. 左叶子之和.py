# https://leetcode-cn.com/problems/sum-of-left-leaves/
# 给定二叉树的根节点 root ，返回所有左叶子之和。

# 迭代法，前中序遍历都可以，只要明确如何判断左叶子的条件就行
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            # 左叶子=左孩子不为空，且左孩子是叶结点
            if curr.left:
                if not curr.left.left and not curr.left.right:
                    res += curr.left.val
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return res

# 解法2：递归，每个递归计算的是其左叶子的值
# 总和=左子树左叶子的值+右子树左叶子的值+当前结点左叶子的值
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        mid = 0
        if root.left and not root.left.left and not root.left.right:
            mid = root.left.val
        return mid + left + right