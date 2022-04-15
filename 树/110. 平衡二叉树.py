# https://leetcode-cn.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解法一：递归
# 递归遍历左子树和右子树，如果两边高度差小于1，返回实际高度
# 否则直接返回-1，表示非高度平衡二叉树
# 递归终止条件为遍历到叶子结点，其高度为0
# 递归最重要的3个点：
#   1. 返回值和入参，本题显然返回值是层高，入参就是当前结点
#   2. 确定终止条件，本题是当前结点是空结点，则终止，返回高度0
#   3. 确定单层循环逻辑，本题的单层循环，就是指当前结点如何判断是否二叉平衡树
#       那么显然，如果左右子树高度>1，就返回-1，表示已经不是平衡二叉树
#       或者左右子树中，有一个不是平衡二叉树，那么也直接返回-1
#       如果是平衡二叉树，那么就计算当前的高度，便于上层结点继续计算是否平衡二叉树
class Solution:
    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        if left == -1:
            return -1
        right = self.getDepth(root.right)
        if right == -1:
            return -1
        if abs(left - right) >= 2:
            return -1
        else:
            return max(left, right) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        res = self.getDepth(root)
        return False if res == -1 else True




